# Change Log

## Chunking Strategy:
- Reverted to `RecursiveCharacterTextSplitter` with chunk size 1000 and overlap 200 after `MarkdownTextSplitter` showed worse overall performance.

