# Change Log

## Chunking Strategy:
- Replaced `RecursiveCharacterTextSplitter` with `MarkdownTextSplitter` to better handle structural elements of the knowledge base.
- Experimented with chunk sizes, settling on 300 characters with a 50-character overlap to improve retrieval precision for specific insurance clauses and employee details.

## Encoder Selection:
- Upgraded the embedding model from `all-MiniLM-L6-v2` to `all-mpnet-base-v2` to leverage a larger model for better semantic understanding of insurance contracts and professional bios.

## Retrieval Tuning:
- Increased `RETRIEVAL_K` from 3 to 5 to provide the LLM with more context, which is particularly useful given the smaller chunk sizes implemented previously.
