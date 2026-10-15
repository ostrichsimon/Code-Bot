# backend

Python-/FastAPI-Backend (geplant). **Stand Phase 0:** nur Grundgerüst – `app/main.py` enthält einen Platzhalter-Endpunkt `GET /api/health` ohne Logik. Keine RAG-Pipeline, keine PDF-Verarbeitung, keine Embeddings, keine Datenbank, keine Ollama-Verbindung.

Struktur: `app/api`, `app/ingestion`, `app/retrieval`, `app/embeddings`, `app/vector_store`, `app/llm`, `app/schemas`, `app/core`, `tests/`, `scripts/` (jeweils mit eigener README).

Abhängigkeiten sind absichtlich minimal (nur `fastapi`). Spätere Abhängigkeiten (Pydantic-Settings, PDF-Parser, Chroma, Sentence Transformers, Ollama-Client) werden erst mit der jeweiligen Phase ergänzt. Startbefehle folgen später.
