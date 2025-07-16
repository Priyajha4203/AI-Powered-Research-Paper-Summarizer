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


## 📁 Project Structure
```bash
AI-Powered-Research-Paper-Summarizer/
│
├── main.py # Main Streamlit app
├── prompt_generator.py # Generate the prompt
├── template.json # Prompt template used by LangChain
├── Logo/
│ ├── background4.png # Background image
│ └── Research_tool_logo.png # Logo image
├── .env # Contains OPENAI_API_KEY
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```
## 💻 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Priyajha4203/AI-Powered-Research-Paper-Summarizer.git

cd AI-Powered-Research-Paper-Summarizer
```
### 2. Create Virtual Environment
```bash
python -m venv venv

source venv/bin/activate  # Windows: venv\Scripts\activate
```
### 3. Install Requirements
```bash
pip install -r requirements.txt
```
### 4. Add OpenRouter API Key

Create a .env file in the root with:
```bash
OPENAI_API_KEY=your_openrouter_api_key
```
🔑 Get a free key from https://openrouter.ai

### 5. Run the App
```bash
streamlit run app.py
```

## 📸 Screenshots

<img width="1889" height="919" alt="image" src="https://github.com/user-attachments/assets/a75d6996-da84-4a1f-af9b-c07c920ce03e" />


## 🔍 Use Cases

📖 Students exploring AI research

🎓 Researchers reviewing foundational papers

👨‍💻 Developers looking for code-centric explanations

## 🌟 Upcoming Features

📄 PDF Upload & Auto Title Extraction

🧠 Section-wise (abstract, methods, conclusion) summaries

🌐 Integration with arXiv & Semantic Scholar APIs

💬 Chat with paper summary (QA interface)


## 🤝 Contributors

### 👤 Priya Jha  
🔗 [LinkedIn](https://www.linkedin.com/in/priya-jha-66a2841a7/)  
🐙 [GitHub](https://github.com/Priyajha4203)

🙌 Contributions are welcome! Feel free to submit a pull request or raise an issue.

