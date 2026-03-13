# Change Log

## Chunking Strategy:
- Reverted to `RecursiveCharacterTextSplitter` with chunk size 1000 and overlap 200 after `MarkdownTextSplitter` showed worse overall performance.
- Updated `RecursiveCharacterTextSplitter` to use a `chunk_size` of 512 and `chunk_overlap` of 100 to test for improved retrieval granularity.

## Retrieval Tuning:
- Increased `RETRIEVAL_K` to 20 to provide a broader context window for the LLM to synthesize answers from multiple document fragments.

## Prompt Engineering:
- Updated `SYSTEM_PROMPT` in `implementation/answer.py` to enforce strict source citation using `[Source: filename/page]` and a structured response format (Direct answer, Supporting details, Disclaimers, Next steps).
- Added explicit instructions to acknowledge conflicting information and avoid speculation.

