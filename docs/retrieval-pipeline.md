# Retrieval-Pipeline

**Status:** 🗓️ geplant, nichts implementiert. Dense vs. Hybrid, Reranker, Embedding-Modell: ❓ offen.

- **Embeddings:** lokal (BGE-M3 oder Alternative) für Chunks und Anfragen.
- **Vektorsuche:** Chroma zuerst; Qdrant als Alternative.
- **Hybride Suche:** semantisch + Keyword/BM25, da exakte Begriffe wichtig sind (ABAP-Klassen, Methoden, CDS-Entities, UI5-Controls, OData-Services, Transaktionscodes, Interfaces, Tabellen-/Feldnamen).
- **Filter:** Dokument, Sprache, Version, Themenbereich.
- **Reranking:** optional, Wahl offen.
- **Quellenbewertung:** Relevanz der Treffer für die Antwort.
