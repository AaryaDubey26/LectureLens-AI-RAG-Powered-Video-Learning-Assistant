# EduCore — Intelligent Video Lecture Assistant

An end-to-end Retrieval-Augmented Generation (RAG) Project designed to transform educational video content into a searchable, interactive AI assistant. This tool allows users to ask questions about course material and receive precise answers with timestamps and video references.

---

## Key Features
- Video Processing: Automatically extracts audio from MP4 files.
- AI Transcription: Uses OpenAI Whisper for high-accuracy multilingual transcription and translation.
- Contextual Chunking: Smartly groups transcriptions into meaningful context blocks for better retrieval.
- Vector Search: Leverages Ollama (nomic-embed-text) for local vector embeddings and Cosine Similarity for efficient retrieval.
- Generative Q&A: Integrates with Google Gemini 2.5 Flash to provide natural, context-aware answers.

---

## Tech Stack
- Languages: Python
- AI/ML: OpenAI Whisper, Google Gemini API, Scikit-learn (Cosine Similarity)
- Embeddings: Ollama (nomic-embed-text)
- Data Handling: Pandas, Joblib
- Media: FFmpeg

---

## Hardware Requirements

| Component | Minimum | Recommended (Fast) |
| :--- | :--- | :--- |
| CPU | 6-Core Processor | 8+ Core Processor |
| GPU | N/A (CPU-only) | NVIDIA GPU (10GB+ VRAM) |
| RAM | 16 GB | 32 GB |
| Disk Space | 20 GB | 50 GB (SSD Recommended) |

---

## Prerequisites

1. FFmpeg: Required for audio extraction.
2. Ollama: Required for local embeddings.
   - Run: `ollama pull nomic-embed-text`
3. Google Gemini API Key: Obtain a key from Google AI Studio.

---

## Setup 

1. Install uv (if you haven't already)
   ```bash
   pip install uv
   ```

2. Clone & enter the project
   ```bash
   git clone https://github.com/swapnilgour18/notesage.git
   cd notesage
   ```

3. Create a virtual environment with uv
   ```bash
   uv venv
   ```

4. Activate it
   ```bash
   # Windows
   .venv\Scripts\activate

   # Mac/Linux
   source .venv/bin/activate
   ```

5. Install dependencies
   ```bash
   uv pip install -r requirements.txt
   ```

6. Add your Gemini API key 
   Create a .env file in the project root:
   ```env
   GEMINI_API_KEY=your_actual_key_here
   ```

### Returning to the project
Every time you return to the project, activate the venv:
```bash
# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

---

## Execution Workflow

Follow these steps in order to build your knowledge base:

| Step | Script | Action |
| :--- | :--- | :--- |
| 1 | `python scripts/01_video_to_mp3.py` | Extracts audio from `data/raw/` to `data/processed/audios/`. |
| 2 | `python scripts/02_mp3_to_json.py` | Transcribes audio to `data/processed/transcripts/` using Whisper. |
| 3 | `python scripts/03_merge_chunks.py` | Merges fragments into larger blocks in `data/processed/chunks/`. |
| 4 | `python scripts/04_generate_embeddings.py` | Generates vector database in `data/vector_db/`. |
| 5 | `python scripts/05_chat.py` | Start Chatting! Ask questions about your content. |

---

## Project Structure
- `scripts/`: Numbered Python scripts for the end-to-end process.
- `data/raw/`: Place your source MP4 files here.
- `data/processed/`: Contains audios, transcripts, chunks, and debug logs.
- `data/vector_db/`: Stores the searchable knowledge base (`embeddings.joblib`).

---

## Security Note
This project uses a `.gitignore` to ensure that sensitive information like `.env` and large media files are not pushed to GitHub. Always keep your API keys private.
