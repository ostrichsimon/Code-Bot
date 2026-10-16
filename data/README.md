# data

Lokale Datenablage des Projekts. **Nur `README.md` und `.gitkeep` werden versioniert** (siehe `.gitignore`).

| Ordner | Inhalt |
|---|---|
| `books/` | Originale SAP-Bücher und umfangreiche PDFs |
| `documents/` | Kleinere/zusätzliche Dokumente (Markdown, HTML, Text, Codebeispiele, Notizen) |
| `processed/` | Verarbeitete Zwischenformate (Text, Überschriften, Chunks, Metadaten) |
| `embeddings/` | Erzeugte bzw. exportierte Embeddings |
| `chroma/` | Persistente lokale ChromaDB |

Benutzer kopieren ihre Dateien **selbst lokal** in die Ordner. Originale bleiben unverändert.
**Stand:** Es ist keine Verarbeitung implementiert (Phase 0). Details: [../docs/data-management.md](../docs/data-management.md).
