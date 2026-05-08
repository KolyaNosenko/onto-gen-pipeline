# Master's Thesis: Knowledge Extraction & Ontological Knowledge Base

Магістерська робота на тему «Розробка системи видобування знань з природномовного
тексту та побудова онтологічної бази знань з використанням дескриптивних логік».

Репозиторій містить дві частини:

- **`thesis/`** — LaTeX-джерела самої дипломної роботи.
- **`src/og_agents/`** — Python-реалізація (агентний пайплайн на LangGraph
  + OpenAI + rdflib/owlready2), що генерує OWL/RDF онтології з природномовного
  тексту. Це практична частина, описана в розділі 4.

## LaTeX (`thesis/`)

Збірка PDF (потрібен TeX Live з `latexmk` та `biber`):

```bash
cd thesis
latexmk -pdf main.tex
```

Результат — `thesis/main.pdf`.

## Python (`src/og_agents/`)

Залежності керуються через [Poetry](https://python-poetry.org/) (Python 3.13).

```bash
poetry install
cp .env.example .env   # заповнити MODEL_PROVIDER_API_KEY та інші змінні
```

Запуск CLI-демо (генерує онтологію з прикладного тексту):

```bash
poetry run python -m og_agents
```

Streamlit UI (чат, перегляд онтології, візуалізація workflow):

```bash
poetry run streamlit run src/og_agents/app/1_Chat.py
```

Перелік потрібних змінних оточення див. у `.env.example`.

## Матеріали

`materials/` — наукові статті, специфікації OWL/RDF та офіційні документи,
використані під час підготовки роботи (не є частиною збірки).
