import shutil
from pathlib import Path

from og_agents.coding_agent.coding_agent import (
    CodingAgent,
    CodingAgentError,
    RESULT_FILE_NAME,
)

_HERE = Path(__file__).resolve().parent
MAIN_TEMPLATE_PATH = _HERE / "coding_agent_main.py"
MAIN_NO_CORE_TEMPLATE_PATH = _HERE / "coding_agent_main_no_core.py"
OUTPUT_TEMPLATE_PATH = _HERE / "coding_agent_output.txt"

# Files/dirs in env that survive reset_workspace (committed structure).
_PRESERVE_NAMES = frozenset(
    {".gitkeep", "__init__.py", "core", "engine", "AGENTS.md"}
)


def reset_workspace(
    env_dir: Path,
    *,
    main_template: Path,
    output_template: Path = OUTPUT_TEMPLATE_PATH,
) -> None:
    env_dir = Path(env_dir)
    env_dir.mkdir(parents=True, exist_ok=True)
    for item in env_dir.iterdir():
        if item.name in _PRESERVE_NAMES:
            continue
        if item.is_dir() and not item.is_symlink():
            shutil.rmtree(item)
        else:
            item.unlink()
    shutil.copy(main_template, env_dir / "main.py")
    shutil.copy(output_template, env_dir / RESULT_FILE_NAME)


__all__ = [
    "CodingAgent",
    "CodingAgentError",
    "RESULT_FILE_NAME",
    "MAIN_TEMPLATE_PATH",
    "MAIN_NO_CORE_TEMPLATE_PATH",
    "OUTPUT_TEMPLATE_PATH",
    "reset_workspace",
]
