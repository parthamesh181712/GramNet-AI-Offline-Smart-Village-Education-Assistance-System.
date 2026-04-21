## GramNet AI – Offline Smart Village Education System

## Overview

GramNet AI is a multilingual offline AI tutor designed to provide personalized and accessible education in rural and low-internet areas. The system supports both text and voice interaction and delivers accurate, context-aware responses using advanced AI techniques.

## Features
Multilingual Support (English, Hindi, Marathi)

Voice Input (Speech-to-Text)

Voice Output (Text-to-Speech)

Retrieval-Augmented Generation (RAG)

TinyLLaMA-based Response Generation

NCERT-based Knowledge System

Adaptive Quiz Engine (Dynamic Difficulty)

Works in Offline Mode


## Technologies Used
Python

TinyLLaMA (LLM)

RAG (Retrieval-Augmented Generation)

NLP (Natural Language Processing)

SpeechRecognition / Whisper (STT)

gTTS / pyttsx3 (TTS)

Vector Database (for semantic search)


## System Architecture
User Input (Text/Voice)

Speech-to-Text (if voice input)

Language Detection

Translation to English

Embedding Generation

Vector Database Retrieval (RAG)

Response Generation (TinyLLaMA)

Translation to User Language

Text-to-Speech Output


## How It Works
User asks a question via text or voice

System processes and translates input

Relevant data is retrieved using embeddings

AI model generates accurate answers

Output is given in user’s language (text/voice)

Quiz adapts based on user performance


## Applications
Smart AI Tutoring System

Rural Education Platforms

Voice-Based Learning Assistant

School and Self-Learning Support


## Results
Accurate answers using RAG

Improved learning with adaptive quizzes

Supports multilingual interaction

Works without internet connectivity


## Conclusion

GramNet AI provides an efficient and intelligent learning solution by combining multilingual support, voice interaction, and adaptive learning. It is especially useful for rural areas where access to quality education and internet is limited.

## Future Scope
Add more regional languages

Improve quiz analytics and tracking

Mobile application development

Integration with real-time datasets


## How to Run

1. Install dependencies:
    pip install -r requirements.txt

2. Run API:
    uvicorn api.main:app --reload

3. Test in browser:
    http://127.0.0.1:8000/
