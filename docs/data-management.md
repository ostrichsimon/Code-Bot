# Datenverwaltung

**Vorhanden:** Ordnerstruktur unter `data/` mit `.gitkeep`/README und `.gitignore`-Regeln. **Geplant:** Verarbeitung. **Offen:** Versionsverwaltung von Dokumenten.

## Ablage
- `data/books/` – Original-Bücher/PDFs (ggf. Unterordner `sapui5/`, `abap/`, `cds/`, `odata/`, `gateway/`)
- `data/documents/` – kleinere Zusatzdokumente
- `data/processed/` – Zwischenformate, Chunks, Metadaten
- `data/embeddings/` – Embedding-Exporte
- `data/chroma/` – lokale ChromaDB

## Lebenszyklus (geplant)
Original (unverändert) → Verarbeitung nach `processed/` → Embeddings → Vektordatenbank. Verarbeitete Daten sind aus den Originalen reproduzierbar.

## Rechte und Lokalität
- Benutzer kopieren Dateien selbst lokal; nichts wird committed (große/vertrauliche Daten per `.gitignore` ausgeschlossen).
- SAP-Bücher unterliegen oft Urheber-/Lizenzrechten; nur Dokumente mit Verarbeitungsrechten verwenden.
- Keine Übertragung an externe Dienste; Logs ohne unnötige Dokumentinhalte.
- Zu erhaltende Metadaten: Titel, Quelle, Sprache, Version, Seitenzahl.
