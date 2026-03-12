# Project Rules

## Files
- `implementation/ingest.py` - Main file I'm working on
- `change_log.md` - Summary of the changes made in this session 
- `requirements.txt` - List of dependencies for the project
- `Readme.md` - General overview of the project and instructions for setup and usage
- `app.py` - Runs the RAG system. Don't change this!

## Rules
- I am an expert in LLMs and RAG, so I should leverage that expertise to improve the performance of the system.
- I can edit `implementation/ingest.py` and `implementation/answer.py` to implement my ideas for improving the RAG system.
- I should edit `change_log.md` for context on the project and to update the current the status of the current task.
- I can edit `requirements.txt` if I need to add any new dependencies for the TTS functionality.
- I can refer to `Readme.md` for more details on the current task.
- I should ask questions if I'm not sure.

## Current Task
### Improve RAG System performance metrics of InsureLLM.
Week steps to complete: create app for user interface that leverages retrieval-augmented generation (RAG) to create intelligent responses based on user queries, enhancing the overall user experience.

### Task Steps:
1. **Chunking Strategy:** experiment with chunking strategy to optimize for your commercial goal
2. **Encoder:** select the best Encoder model and k value based on a test set. A
    - Add selector to the app to allow for dynamic selection of the encoder and k value.
      - Add models to test:
        models_to_test = [
      "all-MiniLM-L6-v2",                          # Your current (fast/light)
      "BAAI/bge-small-en-v1.5",                    # Better performance, still small
      "intfloat/e5-large-v2",                       # Higher quality, slower
    ]
3. **Improve Prompts:** general content, the current date, relevant context and history.



**Files to Edit:**
- `ingest.py` - Main consolidated file for the project. 
- `answer.py` - Update task status. 
- `change_log.md` - Update week section. 
- `requirements.txt` - Update dependencies. 

