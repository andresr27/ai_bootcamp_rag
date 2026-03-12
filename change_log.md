# Change Log

## Week 1: Chunking R&D
- Replaced `RecursiveCharacterTextSplitter` with `MarkdownTextSplitter` to better handle structural elements of the knowledge base.
- Experimented with chunk sizes, settling on 300 characters with a 50-character overlap to improve retrieval precision for specific insurance clauses and employee details.
