# 🤖 AI Agent API

A simple AI Agent built using **FastAPI** and **Groq Llama 3.3**.

## 🚀 Features

- FastAPI Backend
- REST API (`/chat`)
- AI Responses using Groq LLM
- Streaming Responses
- Environment Variable Support
- Modular Project Structure

---

## 📂 Project Structure

```text
AI_Agent/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   ├── models.py
│   ├── agent.py
│   ├── stream.py
│   ├── config.py
│   └── prompts.py
│
├── .env
├── requirements.txt
├── README.md
├── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository_url>
```

Move into the project:

```bash
cd AI_Agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
GROQ_API_KEY=your_api_key_here
```

Run the server:

```bash
uvicorn app.main:app --reload
```

---

## 📖 API Documentation

Open your browser:

```
http://127.0.0.1:8000/docs
```

---

## 🧠 Tech Stack

- Python
- FastAPI
- Groq API
- Llama 3.3 70B
- Uvicorn

---

## 👨‍💻 Author

**Piyush Kotkar**