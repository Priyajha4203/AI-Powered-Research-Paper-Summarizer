# 🤖 AI-Powered Research Paper Summarizer

This is a Streamlit-based intelligent web app that summarizes cutting-edge research papers using large language models. This tool enables summarization of foundational papers across key AI domains in beginner-friendly, technical, or code-oriented styles—all within a visually modern interface.

## 🚀 Features

- 🔍 **Category-Based Research Paper Selection**
- 🧠 **LLM-Powered Summarization** via OpenRouter
- 🎨 **Explanation Styles**: Beginner-Friendly, Technical, Code-Oriented, and Mathematical
- 📏 **Customizable Summary Length**: Short, Medium, Long
- 🌐 **Beautiful UI** using Streamlit and CSS-enhanced background/logo
- 📚 **Preloaded Paper Titles** across AI domains

## 🛠️ Tech Stack

| Area         | Tech Used                           |
|--------------|--------------------------------------|
| 🧠 LLM        | Qwen3-30B-A3B via OpenRouter        |
| 🌐 Framework | Streamlit                          |
| 📦 Orchestration | LangChain                      |
| 🔐 API Keys   | Python-dotenv (.env)               |
| 📄 Prompt Mgmt| LangChain PromptTemplate (JSON)    |
| 🖼️ Design     | Background + Logo (base64 HTML/CSS) |

---

## 📁 Project Structure
```bash```
AI-Powered-Research-Paper-Summarizer/
│
├── app.py # Main Streamlit app
├── template.json # Prompt template used by LangChain
├── logo/
│ ├── background4.png # Background image
│ └── Research_tool_logo.png # Logo image
├── .env # Contains OPENAI_API_KEY
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## 💻 Setup Instructions

### 1. Clone the Repository
```bash```
git clone https://github.com/yourusername/AI-Powered-Research-Paper-Summarizer.git
cd AI-Powered-Research-Paper-Summarizer

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate

### 3. Install Requirements

pip install -r requirements.txt

### 4. Add OpenRouter API Key
Create a .env file in the root with:

OPENAI_API_KEY=your_openrouter_api_key
🔑 Get a free key from https://openrouter.ai

### 5. Run the App

streamlit run app.py

🔍 Use Cases
📖 Students exploring AI research

🎓 Researchers reviewing foundational papers

👨‍💻 Developers looking for code-centric explanations

