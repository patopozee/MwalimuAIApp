# 📚 Mwalimu AI App

## 🚀 Project Overview

Mwalimu AI is an AI-powered personalized learning assistant designed to provide students with a friendly, adaptive, and engaging educational experience.

The project was inspired by modern AI educational platforms that use Large Language Models (LLMs) to generate personalized learning content, adapt explanations to individual student needs, and eventually track progress over time.

The goal of Mwalimu AI is to grow from a simple AI tutor into a complete intelligent learning platform with:

* Personalized student profiles
* Adaptive teaching methods
* AI-generated quizzes
* Student progress tracking
* Subject-specific knowledge systems
* AI agents for teaching, testing, and learning planning

---

# 🌟 Current Features (Version 0.1)

### 🤖 AI-Powered Teacher

Mwalimu AI uses Google's Gemini 2.5 Flash model to answer student questions.

The AI is instructed to:

* Explain concepts according to the student's age and grade level
* Use practical examples
* Adapt explanations based on the student's learning style
* Communicate in the student's preferred language (English, Kiswahili, or Sheng)
* Encourage and support the student

---

### 👨‍🎓 Student Profile System

Each student currently has a profile containing:

* Name
* Grade
* Age
* Favorite subject
* Weak subject
* Learning style
* Preferred language

The student profile is injected into the AI prompt to create personalized responses.

Current implementation uses a `student.py` file with a predefined student profile.

Future versions will allow students to create and edit their profiles through the web interface.

---

### 🌐 Streamlit Web Application

The application provides a simple and interactive user interface.

Features:

* Student profile sidebar
* Question input form
* AI-generated answers
* Loading animation while the AI is thinking
* Automatic clearing of the input field after submission
* Session state memory to preserve the latest question and answer

---

## 🏗️ Project Architecture

```
                     Student
                        |
                        v
                 Streamlit Interface
                      (web.py)
                        |
                        v
               ask_mwalimu()
                      (app.py)
                        |
                        v
              Google Gemini API
                (gemini-2.5-flash)
                        |
                        v
                Personalized Answer
```

---

# 📂 Project Structure

```
mwalimu-ai/
│
├── app.py              # Main AI engine and Gemini integration
│
├── web.py              # Streamlit frontend application
│
├── student.py          # Stores student profile information
│
├── .env                # Environment variables (API key)
│
├── requirements.txt    # Python dependencies
│
└── README.md           # Project documentation
```

---

# 🛠️ Technology Stack

### Programming Language

* Python

### AI Model

* Google Gemini 2.5 Flash

### AI SDK

* Google Gen AI SDK (`google-genai`)

### User Interface

* Streamlit

### Environment Management

* Python virtual environments (`venv`)

### Configuration

* Python dotenv

---

# ⚙️ Installation Guide

## 1. Clone the Repository

```
git clone <repository-url>
cd mwalimu-ai
```

## 2. Create a Virtual Environment

### Windows

```
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS

```
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```
pip install -r requirements.txt
```

Example `requirements.txt`:

```
streamlit
google-genai
python-dotenv
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Running the Application

Start the Streamlit application:

```
streamlit run web.py
```

The application will open in your browser, usually at:

```
http://localhost:8501
```

---

# 🧠 How Mwalimu AI Works

1. The student enters a question through the Streamlit interface.

2. `web.py` sends the question and student profile to `ask_mwalimu()`.

3. `app.py` constructs a personalized prompt containing:

* Student information
* Learning preferences
* Teaching instructions
* The student's question

4. The prompt is sent to Gemini 2.5 Flash.

5. Gemini generates a personalized answer.

6. The answer is displayed to the student in the web interface.

---

# 🔒 Environment Variables

The application requires the following environment variable:

| Variable       | Description                                 |
| -------------- | ------------------------------------------- |
| GEMINI_API_KEY | API key used to access Google Gemini models |

Never commit your `.env` file or API keys to GitHub.

---

# 🗺️ Roadmap

## Version 0.2

* Replace `student.py` with a dynamic student registration form
* Allow students to enter their own name, grade, language, and learning style
* Improve the user interface

## Version 0.3

* Add a database (SQLite/PostgreSQL)
* Store student profiles
* Save learning history and progress
* Create personalized learning recommendations

## Version 0.4

* AI Quiz Generator Agent
* Automatic marking and feedback
* Performance reports
* Strength and weakness analysis

## Version 1.0

* Upload textbooks and PDF notes
* Implement Retrieval-Augmented Generation (RAG)
* Create subject-specific context packs
* Improve factual accuracy

## Version 2.0

A complete AI learning ecosystem featuring:

* Teacher Agent
* Quiz Creator Agent
* Examiner Agent
* Learning Planner Agent
* Progress Analysis Agent

---

# 🎯 Long-Term Vision

Mwalimu AI aims to become an intelligent AI tutor that understands each student as an individual, adapts to their learning style, tracks their progress, and provides high-quality personalized education for students in Kenya and around the world.

---

# 👨‍💻 Developer Notes

This project is being built step-by-step as a learning journey into:

* AI engineering
* Large Language Model (LLM) applications
* Prompt engineering
* AI personalization
* Agent-based AI systems
* Educational technology

Each version introduces new concepts while maintaining a clean and scalable architecture.
