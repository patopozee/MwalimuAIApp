# 📚 Mwalimu AI App

Mwalimu AI is an interactive educational web application designed to act as a friendly, supportive Kenyan teacher. It leverages Google's advanced Large Language Models to explain school concepts simply, offer practical examples, and provide students with continuous encouragement.

The application features a modern, clean chat-like user interface built with Streamlit, optimized to display historical insights prominently while making question submission effortless.

---

## 🚀 Features

* **Mwalimu Persona:** Empathetic, engaging, and culturally contextualized explanations.
* **Optimized UI:** A structured screen layout where responses are prioritized at the top, keeping inputs stable at the bottom.
* **Asynchronous UX:** Instantaneous input field clearing upon submission alongside real-time processing indicators ("*Mwalimu AI is thinking...*").
* **Session Management:** Built-in persistence layer via Streamlit session state to safeguard context over ongoing user iterations.

---

## 🛠️ Tech Stack

* **Frontend UI:** [Streamlit](https://streamlit.io/)
* **GenAI Engine:** Official Google `google-genai` SDK
* **LLM Model Core:** `gemini-2.5-flash`
* **Environment Management:** `python-dotenv`

---

## 📦 Project Structure

```text
MwalimuAIApp/
│
├── venv/                   # Python Virtual Environment
├── .env                    # Secret Environment Variables (API Keys)
├── .gitignore              # Files excluded from GitHub tracking
├── app.py                  # Core backend module interfacing with Gemini API
├── web.py                  # Streamlit user interface implementation
└── README.md               # Project documentation