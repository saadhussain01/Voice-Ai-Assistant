# Voice-Ai-Assistant

An intelligent voice-enabled assistant built with Python, OpenAI, and Streamlit/Gradio. The assistant can listen, respond, remember conversations, and process files (like PDFs) to summarize or answer questions.

# Features

### Voice Interaction – Converts speech to text (STT) and responds with natural text-to-speech (TTS).

### Memory – Remembers past interactions using vector databases (FAISS).

### File Tools – Reads and summarizes PDF documents for quick insights.

### AI-Powered – Uses OpenAI LLM for natural conversation and task execution.

### Interactive UI – User-friendly interface built with Streamlit/Gradio.

# Tech Stack:
Python, OpenAI API, SpeechRecognition, pyttsx3 / gTTS, LangChain, Gradio / Streamlit, FAISS, PyPDF2

# Project Description:
Designed and developed an advanced voice-controlled AI assistant capable of understanding natural language, executing tasks, and interacting with the user through speech. Integrated memory and file-reading tools to enhance assistant capabilities.

1. Implemented voice-to-text (STT) and text-to-speech (TTS) using SpeechRecognition and pyttsx3/gTTS to enable real-time voice interaction.

2. Integrated OpenAI LLM for natural language understanding and task execution including summarization, question answering, and conversation.

3. Built file processing tools to extract and summarize content from PDFs and other documents using PyPDF2 and LangChain’s document loaders.

4. Added memory capabilities with FAISS vector store to allow the assistant to remember and recall past interactions and context.

5. Developed an intuitive Gradio/Streamlit frontend to allow voice interactions, task triggers, and document uploads via a simple GUI.

6. Modularized architecture to support future extensions like calendar scheduling, web scraping, or email automation

