
from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Callable

from openhands.sdk.event.base import Event
from openhands.sdk.event.condenser import (
    Condensation,
    CondensationSummaryEvent,
)
from openhands.sdk.event.llm_completion_log import LLMCompletionLogEvent
from openhands.sdk.event.llm_convertible.action import ActionEvent
from openhands.sdk.event.llm_convertible.message import MessageEvent
from openhands.sdk.event.llm_convertible.observation import (
    AgentErrorEvent,
    ObservationEvent,
)
from openhands.sdk.event.llm_convertible.system import SystemPromptEvent


_SLUG_RE = re.compile(r"[^a-zA-Z0-9_.-]+")


def _slug(text: str, max_len: int = 40) -> str:
    s = _SLUG_RE.sub("-", text).strip("-")
    return s[:max_len] or "run"


def _content_hash(*parts: str | None) -> str:
    h = hashlib.sha256()
    for part in parts:
        h.update((part or "").encode("utf-8"))
        h.update(b"\x00")
    return h.hexdigest()[:8]


def _short_time(iso: str) -> str:
    try:
        return datetime.fromisoformat(iso).strftime("%H:%M:%S")
    except (TypeError, ValueError):
        return iso


def _fence(text: str, lang: str = "") -> str:
    fence = "```"
    while fence in text:
        fence += "`"
    return f"{fence}{lang}\n{text}\n{fence}\n"


def build_log_dir(
    *,
    logs_root: Path,
    model_name: str,
    workspace_name: str,
    fingerprint: str,
) -> Path:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    short_hash = _content_hash(fingerprint)
    dir_name = (
        f"{timestamp}__{_slug(model_name)}__{_slug(workspace_name)}__{short_hash}"
    )
    log_dir = logs_root / dir_name
    log_dir.mkdir(parents=True, exist_ok=True)
    (log_dir / "llm_completions").mkdir(exist_ok=True)
    return log_dir


def _action_render(event: ActionEvent) -> str:
    parts: list[str] = []
    if event.thought:
        thought = "\n".join(b.text for b in event.thought if getattr(b, "text", None))
        if thought.strip():
            parts.append(f"**Thought:**\n\n{thought}\n")
    if event.reasoning_content:
        parts.append(f"**Reasoning:**\n\n{event.reasoning_content}\n")
    tool_call_args: Any = None
    tool_call = event.tool_call
    if tool_call is not None:
        raw = getattr(tool_call, "arguments", None)
        if raw is None:
            raw = getattr(getattr(tool_call, "function", None), "arguments", None)
        if isinstance(raw, str):
            try:
                tool_call_args = json.loads(raw)
            except (ValueError, TypeError):
                tool_call_args = raw
        else:
            tool_call_args = raw
    args_text = (
        json.dumps(tool_call_args, indent=2, ensure_ascii=False)
        if isinstance(tool_call_args, (dict, list))
        else str(tool_call_args)
    )
    parts.append(f"**Tool call:** `{event.tool_name}`\n\n{_fence(args_text, 'json')}")
    return "\n".join(parts)


def _observation_render(event: ObservationEvent) -> str:
    payload = event.observation
    if hasattr(payload, "model_dump"):
        body = json.dumps(payload.model_dump(), indent=2, ensure_ascii=False)
    else:
        body = json.dumps(payload, indent=2, ensure_ascii=False, default=str)
    return f"**Tool:** `{event.tool_name}`\n\n{_fence(body, 'json')}"


def _message_render(event: MessageEvent) -> str:
    blocks = []
    msg = event.llm_message
    if msg is None:
        return "_(empty message)_"
    for content in msg.content or []:
        text = getattr(content, "text", None)
        if text:
            blocks.append(text)
        else:
            blocks.append(repr(content))
    body = "\n\n".join(blocks).strip() or "_(no text content)_"
    return body


def _system_render(event: SystemPromptEvent) -> str:
    sys_prompt = event.system_prompt
    text = ""
    if hasattr(sys_prompt, "text"):
        text = sys_prompt.text or ""
    elif isinstance(sys_prompt, str):
        text = sys_prompt
    else:
        text = json.dumps(sys_prompt, indent=2, default=str)
    tools_summary = []
    for t in event.tools or []:
        name = (
            t.get("function", {}).get("name", "?")
            if isinstance(t, dict)
            else getattr(t, "name", "?")
        )
        tools_summary.append(name)
    tools_line = ", ".join(tools_summary) if tools_summary else "(none)"
    return (
        f"**Tools:** {tools_line}\n\n"
        f"<details><summary>system_prompt ({len(text.splitlines())} lines)</summary>\n\n"
        f"{_fence(text)}\n"
        f"</details>"
    )


def _condensation_render(event: Condensation) -> str:
    summary = event.summary or ""
    forgot = ", ".join(event.forgotten_event_ids or []) or "(none)"
    return (
        f"Forgot {len(event.forgotten_event_ids or [])} events "
        f"(offset {event.summary_offset}). "
        f"Forgotten event ids: {forgot}\n\n"
        f"**Summary:**\n\n> {summary}"
    )


def _condensation_summary_render(event: CondensationSummaryEvent) -> str:
    return f"**Summary:**\n\n> {event.summary}"


def _agent_error_render(event: AgentErrorEvent) -> str:
    return f"**Tool:** `{event.tool_name}`\n\n{_fence(event.error or '', 'text')}"


def _render_markdown(event: Event) -> tuple[str, str]:
    cls = type(event).__name__
    short_ts = _short_time(event.timestamp)
    if isinstance(event, SystemPromptEvent):
        return f"[{short_ts}] SystemPrompt", _system_render(event)
    if isinstance(event, MessageEvent):
        sender = (
            event.sender
            or (event.llm_message.role if event.llm_message else event.source)
        )
        return f"[{short_ts}] {sender} (Message)", _message_render(event)
    if isinstance(event, ActionEvent):
        return (
            f"[{short_ts}] Agent action — {event.tool_name}",
            _action_render(event),
        )
    if isinstance(event, ObservationEvent):
        return (
            f"[{short_ts}] Observation — {event.tool_name}",
            _observation_render(event),
        )
    if isinstance(event, AgentErrorEvent):
        return (
            f"[{short_ts}] AgentError — {event.tool_name}",
            _agent_error_render(event),
        )
    if isinstance(event, Condensation):
        return f"[{short_ts}] Condensation", _condensation_render(event)
    if isinstance(event, CondensationSummaryEvent):
        return (
            f"[{short_ts}] CondensationSummary",
            _condensation_summary_render(event),
        )
    if isinstance(event, LLMCompletionLogEvent):
        return f"[{short_ts}] LLMCompletionLog", f"saved → `{event.filename}`"
    return f"[{short_ts}] {cls}", _fence(json.dumps(event.model_dump(), indent=2, default=str), "json")


def _write_completion(log_dir: Path, event: LLMCompletionLogEvent) -> None:
    safe_name = _slug(event.filename or event.id, max_len=120)
    if not safe_name.endswith(".json"):
        safe_name = f"{safe_name}.json"
    target = log_dir / "llm_completions" / safe_name
    payload = event.log_data
    if isinstance(payload, str):
        # Re-pretty-print if the SDK already serialised the completion to JSON.
        try:
            text = json.dumps(json.loads(payload), indent=2, ensure_ascii=False)
        except (ValueError, TypeError):
            text = payload
    else:
        try:
            text = json.dumps(payload, indent=2, default=str, ensure_ascii=False)
        except TypeError:
            text = repr(payload)
    target.write_text(text, encoding="utf-8")


def make_event_logger(
    *,
    logs_root: Path,
    model_name: str,
    workspace_name: str,
    fingerprint: str,
    run_metadata: dict | None = None,
) -> Callable[[Event], None]:
    log_dir = build_log_dir(
        logs_root=Path(logs_root),
        model_name=model_name,
        workspace_name=workspace_name,
        fingerprint=fingerprint,
    )
    transcript_path = log_dir / "transcript.md"
    events_path = log_dir / "events.jsonl"

    header = [
        f"# Coding agent run\n",
        f"- Model: `{model_name}`",
        f"- Workspace: `{workspace_name}`",
        f"- Started: {datetime.now().isoformat(timespec='seconds')}",
    ]
    if run_metadata:
        for k, v in run_metadata.items():
            header.append(f"- {k}: {v}")
    transcript_path.write_text("\n".join(header) + "\n", encoding="utf-8")

    def _callback(event: Event) -> None:
        try:
            with events_path.open("a", encoding="utf-8") as fh:
                fh.write(
                    json.dumps(
                        {
                            "type": type(event).__name__,
                            **event.model_dump(),
                        },
                        default=str,
                        ensure_ascii=False,
                    )
                )
                fh.write("\n")
            headline, body = _render_markdown(event)
            with transcript_path.open("a", encoding="utf-8") as fh:
                fh.write(f"\n---\n### {headline}\n\n{body}\n")
            if isinstance(event, LLMCompletionLogEvent):
                _write_completion(log_dir, event)
        except Exception as exc:  # pragma: no cover - logging must never break the agent
            try:
                with (log_dir / "logger_errors.log").open("a", encoding="utf-8") as fh:
                    fh.write(f"{datetime.now().isoformat()} {type(exc).__name__}: {exc}\n")
            except OSError:
                pass

    return _callback
