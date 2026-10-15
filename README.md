# Code-Bot – Lokaler SAP-RAG-Chatbot

Lokaler Full-Stack-RAG-Chatbot für **SAP-, ABAP- und SAPUI5-Dokumentation**: Fragen beantworten und Code generieren auf Basis lokal abgelegter SAP-Bücher und Dokumente.

Geplante Eigenschaften: lokale Verarbeitung, lokale Embeddings, lokale Vektordatenbank, lokales LLM über Ollama, React-/TypeScript-Frontend, FastAPI-/Python-Backend.

## Projektstatus

```text
Aktueller Status: Phase 0 – Repository-Struktur und technische Planung

Die eigentliche Implementierung der RAG-Pipeline erfolgt in späteren Arbeitsschritten.
```

**Der Chatbot funktioniert noch nicht.**

| Komponente | Status |
|---|---|
| Repository-Struktur | vorbereitet |
| Dokumentablage | vorbereitet |
| PDF-Ingestion | noch nicht implementiert |
| Chunking | noch nicht implementiert |
| Embeddings | noch nicht implementiert |
| Vektordatenbank | noch nicht implementiert |
| FastAPI-API | nur Grundgerüst |
| Ollama-Anbindung | noch nicht implementiert |
| React-Frontend | nur Grundgerüst |
| Evaluation | geplant |

## Zielarchitektur

Alle Technologien sind **geplant**, sofern nicht anders vermerkt; die Auswahl ist nicht endgültig.

- Python, FastAPI, Pydantic
- PyMuPDF oder eine andere geeignete PDF-Bibliothek (geplant, offen)
- LangChain oder LlamaIndex (geplant, offen)
- HuggingFace/Sentence Transformers (geplant)
- BGE-M3 oder ein später ausgewähltes Embedding-Modell (offen)
- ChromaDB als erster Vektorspeicher (geplant; Qdrant als Alternative offen)
- Ollama als lokale LLM-Schnittstelle (geplant)
- React, TypeScript, Vite (Grundgerüst vorhanden), Tailwind CSS und shadcn/ui (geplant)
- Markdown-Renderer und Syntax-Highlighting (geplant)

Details: [docs/architecture.md](docs/architecture.md).

## Datenfluss

```text
SAP-Buch/PDF
    ↓
Dokumentablage
    ↓
PDF- und Textextraktion
    ↓
Strukturerkennung
    ↓
Chunking
    ↓
Metadatenanreicherung
    ↓
Embedding-Erzeugung
    ↓
Vektordatenbank
    ↓
Benutzerfrage
    ↓
Query-Embedding
    ↓
Retrieval
    ↓
optional Hybrid Search/Reranking
    ↓
Prompt mit Kontext
    ↓
Ollama/LLM
    ↓
Antwort mit Quellen
    ↓
React-Frontend
```

- **Offline-Ingestion:** Einmalig/bei neuen Dokumenten: Extraktion, Strukturerkennung, Chunking, Metadaten, Embeddings, Speicherung. Läuft unabhängig von Benutzerfragen.
- **Online-Fragebeantwortung:** Bei jeder Frage: Query-Embedding, Retrieval, Prompt, Generierung, Antwort.
- **Retrieval:** Findet die relevantesten Chunks zur Frage (semantisch, ggf. hybrid, mit Filtern/Reranking).
- **Prompt-Erzeugung:** Das Backend kombiniert Systemanweisung, Frage und Kontext.
- **LLM-Generierung:** Das lokale Modell formuliert Antwort bzw. Code anhand des Kontexts.
- **Darstellung im Frontend:** Markdown, Syntax-Highlighting, Code kopieren, Quellen anzeigen.

## Dokumentablage

Benutzer kopieren SAP-Bücher und Dokumente **selbst lokal** in die vorgesehenen Ordner:

- `data/books/` – Originale SAP-Bücher und umfangreiche PDFs (optional Unterordner `sapui5/`, `abap/`, `cds/`, `odata/`, `gateway/`)
- `data/documents/` – kleinere/zusätzliche Dokumente (Markdown, HTML, Text, Codebeispiele, Notizen, API-Doku)
- `data/processed/` – verarbeitete Zwischenformate (Text, Überschriften, Chunks, Metadaten)
- `data/embeddings/` – erzeugte/exportierte Embeddings
- `data/chroma/` – lokale persistente ChromaDB

Regeln:
- Originaldateien bleiben unverändert; verarbeitete Dateien liegen getrennt.
- Große Dateien werden nicht in Git versioniert (`.gitignore`; nur `README.md` und `.gitkeep` werden committed).
- Vertrauliche oder lizenzgeschützte Dokumente bleiben lokal.
- Dateinamen sollen nachvollziehbar sein (z. B. `sapui5-data-binding-2024-de.pdf`).
- Metadaten wie Titel, Quelle, Sprache, Version und Seitenzahl sollen später erhalten bleiben.

Siehe [docs/data-management.md](docs/data-management.md).

## Geplantes Chunking

Nicht blind nach Zeichenanzahl teilen. Priorität:

1. Kapitel und Überschriften erkennen.
2. Absätze zusammenhalten.
3. Codeblöcke nicht mitten im Block trennen.
4. Tabellen möglichst separat behandeln.
5. Seiten- und Dokumentmetadaten übernehmen.
6. Nur als Fallback anhand von Tokens oder Zeichenlänge splitten.
7. Ein angemessenes Overlap zwischen Chunks verwenden.

Beispielmetadaten:

```json
{
  "document": "sapui5-data-binding.pdf",
  "page": 142,
  "chapter": "Data Binding",
  "section": "JSONModel",
  "language": "de",
  "content_type": "text",
  "source_type": "book"
}
```

## Geplantes Retrieval

Für SAP-Inhalte ist wahrscheinlich eine Kombination sinnvoll:

- semantische Suche,
- Keyword- bzw. BM25-Suche,
- Filter nach Dokument, Sprache, Version oder Themenbereich,
- optionales Reranking,
- Quellenbewertung.

Exakte Begriffe müssen besonders berücksichtigt werden, weil rein semantische Suche sie leicht verfehlt: ABAP-Klassen, Methoden, CDS-Entities, UI5-Control-Namen, OData-Services, Transaktionscodes, Interface-Namen sowie Tabellen- und Feldnamen.

## Geplante LLM-Anbindung

Ollama dient als lokale Schnittstelle.

- Das Backend baut den Prompt (Systemanweisungen, Benutzerfrage, Retrieval-Kontext).
- Das LLM soll nicht so tun, als wüsste es etwas, wenn der Kontext keine ausreichende Antwort enthält.
- Antworten sollen möglichst Quellen referenzieren.
- Code wird in klaren Markdown-Codeblöcken ausgegeben.
- Modell und Hardware werden später anhand praktischer Tests ausgewählt.

Mögliche Modellkategorien (nichts festgelegt): Coding-Modell, allgemeines Instruct-Modell, mehrsprachiges Modell, kleineres Modell für schwächere Hardware, größeres Modell für bessere Codequalität.

## Geplantes Backend

Verantwortung (alles noch offen): Dokument-Ingestion, Textextraktion, Chunking, Embeddings, Vektorspeicher, Retrieval, Prompt-Aufbau, Ollama-Kommunikation, Quellenverwaltung, Chat-API, Streaming, Konfiguration, Logging, Fehlerbehandlung, Health Checks.

Geplante Endpunkte (nur `GET /api/health` existiert als reiner Platzhalter ohne Logik):

```text
GET  /api/health
POST /api/chat
POST /api/ingest
GET  /api/documents
GET  /api/models
```

Beispielhafte Request-Struktur (Dokumentation, nicht implementiert):

```json
{
  "message": "Erstelle eine UI5-Tabelle mit Kundendaten",
  "conversation_id": "optional",
  "top_k": 5,
  "filters": {
    "document": "optional"
  }
}
```

Geplante Antwort:

```json
{
  "answer": "Später generierte Antwort",
  "sources": [],
  "model": "später festlegen",
  "retrieved_chunks": 0
}
```

## Geplantes Frontend

Chat-Verlauf, Eingabefeld, Senden von Fragen, Streaming, Markdown-Darstellung, Syntax-Highlighting, Copy-Button für Code, Quellenanzeige, Ladezustände, Fehlerzustände, Modellanzeige, Anzeige der verwendeten Dokumente, optional Filter für Dokumente oder Themenbereiche.

Das Frontend kommuniziert später ausschließlich über definierte API-Schnittstellen mit dem Backend. Aktuell existiert nur eine Platzhalteransicht.

## Datenschutz und Sicherheit

- Die Verarbeitung soll lokal erfolgen.
- SAP-Dokumente werden nicht automatisch an externe LLM- oder Embedding-Dienste gesendet.
- Keine Secrets in Git committen; `.env` ist ignoriert, `.env.example` enthält nur Platzhalter.
- Dokumente können vertrauliche oder lizenzrechtlich geschützte Inhalte enthalten.
- API-Zugriff soll später auf lokale Nutzung beschränkt oder abgesichert werden.
- Logs dürfen keine vertraulichen Dokumentinhalte unnötig speichern.

## Entwicklungsphasen

**Phase 0 – Grundgerüst:** Repository-Struktur, README, Dokumentablage, Konfigurationsplatzhalter, technische Entscheidungen dokumentieren.

**Phase 1 – Minimaler PDF-Ingestion-Prototyp:** ein PDF einlesen, Text extrahieren, Seiteninformationen bewahren, Ergebnis lokal speichern.

**Phase 2 – Strukturiertes Chunking:** Überschriften erkennen, Codeblöcke schützen, Metadaten ergänzen, Chunking testen.

**Phase 3 – Embeddings:** lokales Embedding-Modell auswählen, Embeddings erzeugen, Messergebnisse dokumentieren.

**Phase 4 – Vektordatenbank:** Chroma lokal integrieren, Dokumente speichern, einfache semantische Suche.

**Phase 5 – Ollama:** Verbindung herstellen, Modell konfigurieren, Prompt-Aufbau.

**Phase 6 – Chat-API:** FastAPI-Endpunkte, Request-/Response-Schemas, Retrieval plus LLM-Aufruf, Quellen zurückgeben.

**Phase 7 – Frontend:** React-Chat-Oberfläche, API-Integration, Markdown, Code-Rendering, Quellenanzeige.

**Phase 8 – Qualität und Evaluation:** Testfragen, Retrieval-Evaluation, Antwortqualität, Halluzinationen, Codequalität, Laufzeit und Ressourcenverbrauch.

Siehe [docs/development-roadmap.md](docs/development-roadmap.md).

## Evaluationsstrategie

Später wird ein Testdatensatz mit typischen SAP-Fragen angelegt: UI5 Data Binding, JSONModel, OData, ABAP Open SQL, CDS Views, Gateway, RAP, Tabellen und Controls, Fehlerbehandlung, Codegenerierung.

Bewertungskriterien:
- Wurde der richtige Kontext gefunden?
- Sind die Quellen relevant?
- Ist die Antwort fachlich korrekt?
- Ist der Code syntaktisch plausibel?
- Werden Unsicherheiten transparent gemacht?
- Werden Quellen ausgegeben?
- Ist die Antwort reproduzierbar?

Siehe [docs/evaluation.md](docs/evaluation.md).

## Lokale Voraussetzungen (geplant)

Versionen werden später festgelegt; nur grobe Anforderungen:

- Git
- Python (aktuelle Version, später festzulegen)
- Node.js und npm oder pnpm (später festzulegen)
- Ollama
- ausreichend RAM/VRAM, abhängig vom Modell
- lokale SAP-Dokumente
- optional Docker

## Lokaler Start – später geplant

Konkrete Startbefehle werden ergänzt, sobald Backend und Frontend implementiert sind. Aktuell läuft **keine** vollständige Anwendung.

```bash
# Backend – später ergänzen
# cd backend
# python -m ...

# Frontend – später ergänzen
# cd frontend
# npm install
# npm run dev
```

## Offene technische Entscheidungen

- LangChain oder LlamaIndex?
- PyMuPDF oder anderer PDF-Parser?
- Chroma oder Qdrant?
- BGE-M3 oder alternatives Embedding-Modell?
- Welche Chunk-Größe?
- Welche Overlap-Größe?
- Dense Search oder Hybrid Search?
- Welcher Reranker?
- Welches Ollama-Modell?
- SSE oder WebSocket für Streaming?
- Wie werden Dokumentversionen verwaltet?
- Wie werden Quellen im Frontend dargestellt?
- Wie werden Evaluationsdaten gespeichert?

## Lizenz und Dokumentrechte

Der Code steht unter der MIT-Lizenz (siehe [LICENSE](LICENSE)). Diese gilt **nicht** für Dokumente, die du lokal ablegst. Verwende nur Dokumente, für deren lokale Verarbeitung du die erforderlichen Rechte besitzt. SAP-Bücher und -Dokumentationen werden nicht mit dem Repository ausgeliefert.
