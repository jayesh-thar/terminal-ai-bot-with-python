# 🧑‍💻 DeepSeek Terminal Chatbot  

A simple yet powerful terminal-based chatbot built with **Python** that uses the **DeepSeek API** for natural conversations.  
Supports conversation history, `.env` for secrets, and local chat log saving.  

---

## 🚀 Features  
- ✅ Chat with **DeepSeek AI** directly from your terminal  
- ✅ Conversation history within a session  
- ✅ Chat logs saved locally in `chats/`  
- ✅ Uses `.env` to keep your API key safe  
- ✅ Lightweight, runs on any system with Python  

---

## 📂 Project Structure  

terminal-chatbot/
│── .gitignore
│── .env.example
│── README.md
│── requirements.txt
│── src/
│ ├── main.py # Entry point
│ ├── chat_cli.py # Chat logic
│ └── deepseek_api.py # API wrapper
│── chats/
│ └── .gitkeep # Keeps folder in repo


---

## ⚙️ Setup Instructions  

### 1️⃣ Clone the repo  
```bash
git clone https://github.com/<your-username>/terminal-chatbot.git
cd terminal-chatbot
```

### 2️⃣ Create & activate virtual environment
```bash 
python -m venv .venv
# Activate
# Windows (PowerShell)
.venv\Scripts\Activate
# macOS/Linux
source .venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
3️⃣ Install dependencies
```

### 4️⃣ Configure Environment Variables

- Create a file named .env in the project root

``` bash
DEEPSEEK_API_KEY=your_api_key_here
```

### 5️⃣ Run the chatbot

```bash 
python src/main.py
```


### 📖 Usage

Start the chatbot and type messages:

```bash
🤖 DeepSeek Chatbot is ready! Type 'exit' to quit.
You: hi
Bot: Hello! How can I help you today?
```

- Type exit to end the chat.
- Logs are saved in the chats/ folder.


### 👨‍💻 Contributing

Contributions are welcome! To add improvements:
    Fork this repo
    Create a new branch (feature-new)
    Commit your changes
    Open a Pull Request