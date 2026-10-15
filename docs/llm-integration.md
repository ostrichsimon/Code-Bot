# LLM-Integration

**Status:** 🗓️ geplant, keine Ollama-Anbindung vorhanden. Modell ❓ offen (Auswahl nach praktischen Tests/Hardware).

- Ollama als lokale Schnittstelle; das Backend baut den Prompt.
- Prompt: Systemanweisung + Benutzerfrage + Retrieval-Kontext.
- Reicht der Kontext nicht, soll das Modell das offen sagen statt zu raten.
- Quellen referenzieren; Code in Markdown-Codeblöcken.
- Modellkategorien: Coding-Modell, allgemeines Instruct-Modell, mehrsprachiges Modell, kleineres Modell (schwache Hardware), größeres Modell (bessere Codequalität).
- Streaming: SSE oder WebSocket ❓ offen.
