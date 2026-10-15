"""Platzhalter-Einstiegspunkt (Phase 0, vorläufig).

Enthält keine Geschäftslogik. Spätere Chat-, Ingestion- und Dokument-Endpunkte
(siehe docs/architecture.md) werden in eigenen Arbeitsschritten über ``app.api`` eingebunden.
"""

from fastapi import FastAPI

app = FastAPI(title="SAP RAG Chatbot (Platzhalter)", version="0.0.0")


@app.get("/api/health")
def health() -> dict[str, str]:
    """Reiner Platzhalter-Health-Check. Prüft keine Abhängigkeiten."""
    return {"status": "placeholder"}
