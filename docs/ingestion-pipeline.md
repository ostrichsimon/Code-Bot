# Ingestion-Pipeline

**Status:** 🗓️ geplant, nichts implementiert. PDF-Parser (PyMuPDF oder anderer) ❓ offen.

## Schritte
1. Dokument aus `data/books/` bzw. `data/documents/` lesen (Original unverändert).
2. Text- und Strukturextraktion mit Seiteninfos.
3. Normalisierung (Silbentrennung, Kopf-/Fußzeilen, Codeblöcke).
4. Strukturerkennung (Kapitel, Überschriften, Tabellen, Code).
5. Chunking, Ergebnis nach `data/processed/`.

## Chunking-Priorität
1. Kapitel/Überschriften erkennen 2. Absätze zusammenhalten 3. Codeblöcke nicht trennen 4. Tabellen separat 5. Seiten-/Dokumentmetadaten übernehmen 6. Fallback: Token-/Zeichenlänge 7. angemessenes Overlap.

Chunkgröße und Overlap: ❓ offen. Beispielmetadaten:
```json
{"document": "sapui5-data-binding.pdf", "page": 142, "chapter": "Data Binding",
 "section": "JSONModel", "language": "de", "content_type": "text", "source_type": "book"}
```
