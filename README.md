# OpenAI API Programming - Part 2

Example code for the OpenAI Application Explorers meetup:
[OpenAI API Programming - Part 2: Tools, RAG & Advanced Patterns](https://www.meetup.com/practical-chatgpt-api-programming/events/313867024/).

This repo contains small Python examples used to demonstrate tools/function calling, embeddings, vector stores, file search, and fine-tuning workflows with the OpenAI API.

## Meetup Topics

- Function calling and tools
- Embeddings and vector stores
- Retrieval-augmented generation (RAG)
- File search
- Fine-tuning basics and tradeoffs

## Files

- `app.py` - Responses API example with a local `get_horoscope` function tool.
- `app1.py` - Creates an embedding for sample text.
- `app2.py` - Uploads a file, creates a vector store, and attaches the file to it.
- `app3.py` - Queries a response using file search against an existing vector store.
- `create_jsonl.py` - Converts `input_data.json` into JSONL training data.
- `upload_jsonl.py` - Uploads the JSONL file for fine-tuning.
- `create_finetune.py` - Starts a fine-tuning job from an uploaded file.
- `use_finetune_model.py` - Calls a previously fine-tuned model.
- `input_data.json` - Sample fine-tuning training data.

## Setup

Install dependencies:

```powershell
pip install -r requirements.txt
```

Create a local `config.py` file with your OpenAI API key:

```python
OPENAI_API_KEY = "your-api-key-here"
```

Do not commit `config.py` or any real API keys.

## Run Examples

Convert sample training data to JSONL:

```powershell
python create_jsonl.py
```

Run an example script:

```powershell
python app.py
```

Some scripts use hard-coded file IDs, vector store IDs, or fine-tuned model IDs from the live demo. Replace those IDs with resources from your own OpenAI account before running them.

## Notes

These examples are intentionally small and meetup-friendly. They are meant for learning the API building blocks, not as production-ready application structure.
