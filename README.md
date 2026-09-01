# LitigationAI: Enterprise Notice Analyzer & Reply Builder

An architectural prototype developed for the **ICAI Advanced Course on Artificial Intelligence for Chartered Accountants (Level 2) Capstone Project**.

## Directory Layout
- `main.py`: Project entrypoint orchestration.
- `config/settings.py`: Isolate application constants and Legal LLM prompts.
- `services/document_service.py`: Business logic for local text extraction from structural PDFs.
- `services/legal_service.py`: Engine connection for LangChain orchestration.
- `views/dashboard.py`: Frontend User Interface components rendered through Streamlit Mixins.

## Execution
Ensure dependencies are satisfied:
```bash
pip install -r requirements.txt
```
Launch application server:
```bash
streamlit run main.py
```
