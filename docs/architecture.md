# Architektur

**Legende:** ✅ vorhanden · 🗓️ geplant · ❓ offen

## Bereits vorhanden
- ✅ Repository-Struktur, Dokumentablage, Platzhalter-Backend (`GET /api/health`), Platzhalter-Frontend.

## Komponenten und Verantwortlichkeiten (geplant)
| Komponente | Verantwortung | Status |
|---|---|---|
| `ingestion` | PDF-/Textextraktion, Strukturerkennung, Chunking | 🗓️ |
| `embeddings` | lokale Embeddings (BGE-M3 oder Alternative) | ❓ Modell offen |
| `vector_store` | Chroma (erstes Ziel), Qdrant als Alternative | ❓ |
| `retrieval` | semantische/hybride Suche, Filter, Reranking | 🗓️ |
| `llm` | Prompt-Aufbau, Ollama-Kommunikation, Quellen | 🗓️ |
| `api` / `schemas` / `core` | FastAPI-Endpunkte, Pydantic-Schemas, Konfiguration/Logging | 🗓️ |
| Frontend | React, TypeScript, Vite, Tailwind CSS, shadcn/ui, Markdown, Syntax-Highlighting | 🗓️ |

## Datenfluss
**Offline-Ingestion:** Dokument → Extraktion → Struktur → Chunking → Metadaten → Embeddings → Vektordatenbank.
**Online-Fragebeantwortung:** Frage → Query-Embedding → Retrieval (ggf. Hybrid/Reranking) → Prompt mit Kontext → Ollama → Antwort mit Quellen → Frontend.

Alles läuft lokal; es werden keine Dokumente an externe Dienste gesendet.
