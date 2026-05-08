import streamlit as st
from collections import defaultdict
from rdflib import Graph
import streamlit.components.v1 as components

from og_agents.app.dependencies import init_app_dependencies
from og_agents.workflows import WorkflowContext
from og_agents.workflows.nodes import (
    DOCUMENTS_LOADING_NODE_NAME,
    GENERATE_COMPETENCY_QUESTIONS_NODE_NAME,
    GENERATE_ONTOLOGY_NODE_NAME,
    ONTOLOGY_CONSISTENCY_VALIDATION_NODE_NAME,
    ONTOLOGY_RDF_SYNTAX_VALIDATION_NODE_NAME,
    OOPS_ONTOLOGY_VALIDATION_NODE_NAME,
)
from og_agents.app.ontology_visualization import visualize_ontology


st.set_page_config(layout="wide")

app_dependencies = init_app_dependencies()
ontology_storage = app_dependencies.ontology_storage
ontology_generation_workflow = app_dependencies.ontology_generation_workflow

if "is_ontology_exists" not in st.session_state:
    st.session_state.is_ontology_exists = False

INITIAL_LIMIT = 1000

try:
    is_ontology_exists = ontology_storage.is_exist()
    st.session_state.is_ontology_exists = is_ontology_exists
except Exception as e:
    st.error(f"Помилка завантаження онтології: {e}")

if not st.session_state.is_ontology_exists:
    st.title("Онтологію не знайдено, створіть нову")

    uploaded_file = st.file_uploader("Додати файл", type=["txt"])

    if uploaded_file is not None:
        raw_bytes = uploaded_file.read()

        st.header("Створення онтології з тексту:")
        st.caption(raw_bytes.decode("utf-8", errors="ignore"))

        workflow_execution = st.container()
        last_step = None

        llm_placeholders = {}              # step -> st.empty() (created ONLY in custom branch, at the end)
        llm_buffers = defaultdict(str)     # step -> accumulated tokens

        for evt in ontology_generation_workflow.stream(
            {"raw_files": [raw_bytes]},
            context=WorkflowContext(
                config=app_dependencies.app_config,
                http_client=app_dependencies.http_client,
                language_model=app_dependencies.language_model,
                ontology_storage=app_dependencies.ontology_storage,
            ),
            stream_mode=["custom", "messages"],
        ):
            with workflow_execution:
                mode = None
                payload = evt
                if isinstance(evt, tuple):
                    if len(evt) == 3:
                        _namespace, mode, payload = evt
                    elif len(evt) == 2:
                        a, b = evt
                        if isinstance(a, str) and a in ("custom", "messages", "updates", "values", "debug"):
                            mode, payload = a, b
                        else:
                            mode, payload = None, evt

                # ----------------------------
                # 1) LLM token streaming: BUFFER ONLY (never create UI here)
                # ----------------------------
                if mode == "messages":
                    try:
                        msg, metadata = payload
                    except Exception:
                        continue

                    step = metadata.get("langgraph_node") or metadata.get("node") or "LLM"
                    delta = getattr(msg, "content", "") or ""
                    if not delta:
                        continue

                    llm_buffers[step] += delta

                    # Render only if placeholder already exists (created in custom branch)
                    if step in llm_placeholders:
                        llm_placeholders[step].code(llm_buffers[step])

                    continue

                # ----------------------------
                # 2) Your custom stream logic (unchanged `message` semantics)
                # ----------------------------
                chunk = payload
                if not isinstance(chunk, dict) or "current_step" not in chunk:
                    continue

                step = chunk["current_step"]

                if not last_step:
                    st.subheader(f"Поточний крок {step}", divider=True)
                    last_step = step
                elif last_step != step:
                    st.subheader(f"Поточний крок {step}", divider=True)
                    last_step = step

                # ---- your existing rendering (all your writes happen BEFORE LLM placeholder) ----
                if step == GENERATE_COMPETENCY_QUESTIONS_NODE_NAME:
                    st.write(chunk["message"])

                elif step == GENERATE_ONTOLOGY_NODE_NAME:
                    st.write(chunk["message"])

                elif step == ONTOLOGY_RDF_SYNTAX_VALIDATION_NODE_NAME:
                    if "error" in chunk:
                        st.write(chunk["message"])
                        st.warning(chunk["error"])
                    else:
                        st.write(chunk["message"])

                elif step == OOPS_ONTOLOGY_VALIDATION_NODE_NAME:
                    if "error" in chunk:
                        st.write(chunk["message"])
                        st.warning(chunk["error"])
                    else:
                        st.write(chunk["message"])

                elif step == ONTOLOGY_CONSISTENCY_VALIDATION_NODE_NAME:
                    if "error" in chunk:
                        st.write(chunk["message"])
                        st.warning(chunk["error"])
                    elif "ontology_ttl" in chunk:
                        st.write(chunk["message"])
                        # st.code(chunk["ontology_ttl"])
                    else:
                        st.write(chunk["message"])

                else:
                    st.write(chunk.get("message", ""))

                if step not in llm_placeholders:
                    llm_placeholders[step] = st.empty()

                # If tokens already streamed, show them now (still at the end)
                if llm_buffers.get(step):
                    llm_placeholders[step].code(llm_buffers[step])

        else:
            with workflow_execution:
                st.success("Онтологію створено!")
                st.divider()
                st.balloons()
                show = st.button("🚀 Показати онтологію")

                if show:
                    st.session_state.is_ontology_exists = True
                    st.rerun()


@st.dialog("RDF (Turtle)")
def rdf_modal(rdf_graph: Graph):
    ttl_text = rdf_graph.serialize(format="turtle")

    st.download_button(
        "⬇️ Завантажити ontology.ttl",
        data=ttl_text,
        file_name="ontology.ttl",
        mime="text/turtle",
        use_container_width=True,
    )
    st.code(ttl_text, language="turtle")


if st.session_state.is_ontology_exists:
    st.title("Онтологія")

    with st.sidebar:
        st.header("Налаштування графа")

        height = st.slider("Висота (px)", 200, 2000, 700, 50)
        limit = st.slider("Макс. кількість зв'язків", 10, 2000, INITIAL_LIMIT, 10)
        initial_zoom = st.slider("Початковий зум", 0.1, 1.0, 0.8, 0.1)

        st.divider()

        show_schema_only = st.checkbox("📐 Тільки схема (OWL/RDFS)", value=False)
        show_classes = st.checkbox("Класи", True)
        show_object_props = st.checkbox("Object Properties", True)
        show_data_props = st.checkbox("Datatype Properties", True)
        show_individuals = st.checkbox("Індивіди", True)

        st.divider()

        show_labels = st.checkbox("🏷 Показувати назви", False)
        show_comments = st.checkbox("💬 Показувати коментарі", False)
        physics = st.checkbox("🧲 Physics (layout)", True)

        st.divider()

        reset = st.button("🧨 Видалити Онтологію")
        if reset:
            ontology_storage.destroy()
            st.cache_data.clear()
            st.success("Онтологію видалено")
            st.session_state.is_ontology_exists = False
            st.rerun()

    try:
        rdf_graph: Graph = ontology_storage.get_world_as_rdf_graph()

        show_rdf = st.button("📄 Показати RDF (Turtle)")
        if show_rdf:
            rdf_modal(rdf_graph)

        net = visualize_ontology(
            rdf_graph,
            height=height,
            limit=limit,
            show_classes=show_classes,
            show_object_props=show_object_props,
            show_data_props=show_data_props,
            show_individuals=show_individuals,
            show_schema_only=show_schema_only,
            show_labels=show_labels,
            show_comments=show_comments,
            physics=physics,
            initial_zoom=initial_zoom,
        )

        html = net.generate_html()
        components.html(html, height=height + 50, scrolling=True)
    except Exception as e:
        st.error(f"Помилка завантаження графа: {e}")
