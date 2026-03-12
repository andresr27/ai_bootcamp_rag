# Change Log

## Chunking Strategy:
- Reverted to `RecursiveCharacterTextSplitter` with chunk size 1000 and overlap 200 after `MarkdownTextSplitter` showed worse overall performance.

## Retrieval Tuning:
- Increased `RETRIEVAL_K` to 5 to assess if more context improves response quality with the current embedding model.

