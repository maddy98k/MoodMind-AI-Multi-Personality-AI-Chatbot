# 🤖 MoodMind AI — Multi-Personality AI Chatbot

> **One AI. Three Personalities. Your Conversation.**

MoodMind AI is a GenAI-powered chatbot that changes its personality and response style based on the mood selected by the user.

Users can choose between:

- 😡 **Angry Mode** — frustrated, sarcastic, and energetic responses
- 😂 **Funny Mode** — humorous, playful, and entertaining responses
- 😢 **Sad Mode** — emotional, melancholic, and expressive responses

The application is built using **Python, Streamlit, LangChain, and Hugging Face**.

---

## 🚀 Features

- 🤖 AI-powered conversational chatbot
- 🎭 Multiple AI personalities
- 😡 Angry personality
- 😂 Funny personality
- 😢 Sad personality
- 💬 Chat history maintained during the session
- 🔄 Personality changes dynamically
- ⚡ Streamlit-based web interface
- 🔐 Secure API key management using Streamlit Secrets
- 🧠 Powered by a Hugging Face language model
- 🛡️ Basic error handling

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Web interface |
| LangChain | LLM application framework |
| Hugging Face | Model/API provider |
| DeepSeek-R1 | Language model |
| Git & GitHub | Version control |
| Streamlit Community Cloud | Deployment |

---

## 🏗️ Project Architecture

```text
                 ┌─────────────────────┐
                 │       User          │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │     Streamlit UI    │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Select AI Mood    │
                 │                     │
                 │ 😡 Angry            │
                 │ 😂 Funny            │
                 │ 😢 Sad              │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   System Prompt     │
                 │ Personality Control │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │     LangChain       │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    Hugging Face     │
                 │      LLM API        │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    AI Response      │
                 └─────────────────────┘
```

---

## 📁 Project Structure

```text
moodmind-ai-chatbot/
│
├── uichat.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── .streamlit/
    └── secrets.toml       # Local only - DO NOT upload
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/moodmind-ai-chatbot.git
```

### 2. Open the project

```bash
cd moodmind-ai-chatbot
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Key Configuration

This project uses a Hugging Face API token.

Create a Hugging Face account and generate an API token.

For local development, create:

```text
.streamlit/secrets.toml
```

Add:

```toml
HF_TOKEN = "hf_your_token_here"
```

### ⚠️ Important

Never upload your API token to GitHub.

Make sure `.gitignore` contains:

```text
.streamlit/secrets.toml
.env
```

---

## ▶️ Run the Application

Start Streamlit:

```bash
streamlit run app.py
```

The application will normally open at:

```text
http://localhost:8501
```

---

## 🎭 Available AI Modes

### 😡 Angry Mode

The AI responds with an angry, frustrated, and sarcastic personality while avoiding abusive or hateful language.

Example:

```text
User:
Why is Python so easy?

AI:
Seriously? That's exactly why people love it!
Python practically does half the work for you. 😤
```

---

### 😂 Funny Mode

The AI responds with humor and a playful personality.

Example:

```text
User:
Why do programmers like coffee?

AI:
Because without coffee, their code enters
"debugging mode" before they do. ☕😂
```

---

### 😢 Sad Mode

The AI responds with an emotional and slightly melancholic personality.

Example:

```text
User:
How are you?

AI:
I'm just a collection of algorithms...
but today, even my algorithms feel a little tired. 😢
```

---

## 🧠 How It Works

MoodMind AI uses **system prompts** to control the personality of the language model.

For example:

```python
system_prompt = """
You are a Funny AI agent.

Respond with humor, jokes
and a playful personality.
"""
```

The selected personality is sent to the language model together with the conversation history.

This allows the same underlying LLM to behave differently depending on the selected mood.

---

## 🔐 Security

API keys are not stored directly inside the Python source code.

Instead, the application uses:

```python
st.secrets["HF_TOKEN"]
```

For local development:

```text
.streamlit/secrets.toml
```

For Streamlit Cloud, the secret should be configured through the application's **Secrets** settings.

---

## ☁️ Deployment

MoodMind AI can be deployed using Streamlit Community Cloud.

### Deployment steps

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Connect your GitHub account.
4. Select the repository.
5. Select `app.py` as the main file.
6. Add your Hugging Face token to Streamlit Secrets.
7. Deploy the application.

After deployment, Streamlit will provide a public URL.

Example:

```text
https://moodmind-ai-chatbot.streamlit.app
```

---

## 🔄 Future Improvements

Possible improvements include:

- 🧹 Clear chat button
- 🎨 Custom UI themes
- 🎚️ Temperature control
- 🤖 Multiple LLM selection
- 💾 Persistent conversation history
- 📄 RAG document upload
- 📚 PDF question answering
- 🔍 Semantic search
- 🧠 ChromaDB vector database
- 🎤 Voice input
- 🔊 Text-to-speech
- 👤 User authentication
- 📊 Token/usage monitoring

---

## 📌 Future Version

A future version can extend MoodMind AI into a **RAG-based educational chatbot**:

```text
                 User
                   │
                   ▼
             Streamlit UI
                   │
                   ▼
             User Question
                   │
                   ▼
            ChromaDB Search
                   │
                   ▼
              Retriever
                   │
                   ▼
          Relevant Documents
                   │
                   ▼
            Hugging Face LLM
                   │
                   ▼
            Generated Answer
```

This would make the project more suitable as a portfolio-level **GenAI + RAG application**.

---

## 👨‍💻 Author

**Your Name**

GitHub: `https://github.com/YOUR_USERNAME`

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is intended for educational and portfolio purposes.
