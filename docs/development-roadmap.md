# Entwicklungsfahrplan

Aktuell: **Phase 0 (✅ in Arbeit/abgeschlossen mit diesem Schritt)**. Alle weiteren Phasen sind 🗓️ geplant, Details ❓ offen.

| Phase | Inhalt | Abhängig von |
|---|---|---|
| 0 | Struktur, README, Dokumentablage, Konfigurationsplatzhalter, Entscheidungen | – |
| 1 | Minimaler PDF-Ingestion-Prototyp (ein PDF, Text, Seiten, lokal speichern) | 0 |
| 2 | Strukturiertes Chunking (Überschriften, Codeblöcke, Metadaten, Tests) | 1 |
| 3 | Embeddings (Modellwahl, Erzeugung, Messungen) | 2 |
| 4 | Vektordatenbank (Chroma, Speicherung, einfache semantische Suche) | 3 |
| 5 | Ollama (Verbindung, Modellkonfiguration, Prompt-Aufbau) | 4 |
| 6 | Chat-API (Endpunkte, Schemas, Retrieval + LLM, Quellen) | 4, 5 |
| 7 | Frontend (Chat-UI, API, Markdown, Code, Quellen) | 6 |
| 8 | Qualität und Evaluation | 6, 7 |
