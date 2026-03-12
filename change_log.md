# Change Log

## Chunking Strategy:
- Reverted to `RecursiveCharacterTextSplitter` with chunk size 1000 and overlap 200 after `MarkdownTextSplitter` showed worse overall performance.
- Updated `RecursiveCharacterTextSplitter` to use a `chunk_size` of 512 and `chunk_overlap` of 100 to test for improved retrieval granularity.

## Retrieval Tuning:
- Increased `RETRIEVAL_K` to 5 to assess if more context improves response quality with the current embedding model.

