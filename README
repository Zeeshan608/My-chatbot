<div align="center">

# ✨ Nova AI Assistant

### A fast, elegant AI chatbot powered by Google Gemini and built with Streamlit

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Open_App-8B5CF6?style=for-the-badge)](https://my-chatbot-804.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Gemini](https://img.shields.io/badge/Google-Gemini_API-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)

**[👉 Try Nova AI Live](https://my-chatbot-804.streamlit.app/)**

![Nova AI Screenshot](screenshot.png)

</div>

---

## 📖 About the Project

**Nova AI** is a modern, responsive chatbot that lets you talk to Google's Gemini models through a clean, professional interface. It streams answers in real time, lets you switch between different AI models and personas on the fly, and keeps your API key completely secret.

Whether you want to write an email, learn a concept, debug Python code, or brainstorm startup ideas, Nova is ready to help.

---

## 🌟 Key Features

| Feature | Description |
|---|---|
| ⚡ **Real-time streaming** | Answers appear word by word as they are generated, with a live typing cursor |
| 🤖 **Multiple AI models** | Choose from the Gemini models available to your API key, picked from a dropdown |
| 🔄 **Auto-updating model list** | The app asks Google which models are currently available, so it keeps working when models are renamed or retired |
| 🎭 **Switchable personas** | General Assistant, Professional Writer, Coding Mentor, and Study Tutor |
| 🎚️ **Creativity control** | A slider adjusts the temperature from precise to highly creative |
| 💬 **Conversation memory** | The full chat history is sent with every request, so Nova remembers the context |
| 🚀 **Quick-start prompts** | One-click suggestion cards to begin a conversation instantly |
| ⬇️ **Download chat** | Save the whole conversation as a text file |
| 🗑️ **New chat button** | Clear the conversation and start fresh |
| 🎨 **Custom dark UI** | Gradient glow background, glass-style chat bubbles, and a polished sidebar |
| 🔐 **Secure by design** | The API key is never written in code or uploaded to GitHub |
| 🛡️ **Clear error messages** | Real API errors are displayed, which makes troubleshooting easy |

---

## ⚙️ How It Works

```
 ┌──────────────┐     ┌───────────────────┐     ┌──────────────────┐
 │  User types  │ ──▶ │   Streamlit app   │ ──▶ │  Google Gemini   │
 │  a message   │     │ (app.py + CSS UI) │     │       API        │
 └──────────────┘     └───────────────────┘     └──────────────────┘
        ▲                       │                         │
        │                       ▼                         │
        │            ┌───────────────────┐                │
        └─────────── │  Streamed reply   │ ◀──────────────┘
                     │  shown live in UI │
                     └───────────────────┘
```

1. **Secure startup:** the app reads `GEMINI_API_KEY` from Streamlit secrets and connects to the Gemini API.
2. **Model discovery:** it fetches the list of chat models your key can use and fills the **Model** dropdown (Flash models first, since they are faster and work on the free tier).
3. **You send a message:** your message is added to the session history.
4. **The request is built:** the full conversation, the chosen persona (as a system instruction), and the creativity setting are sent to Gemini.
5. **Streaming response:** Gemini sends the answer in small chunks, and Nova displays each chunk instantly.
6. **Memory kept:** the finished reply is saved to the chat history for the next turn.

---

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** [Streamlit](https://streamlit.io/)
- **AI:** [Google Gemini API](https://ai.google.dev/) via the `google-genai` SDK
- **Styling:** Custom CSS (Inter font, gradients, glassmorphism)
- **Hosting:** Streamlit Community Cloud
- **Version control:** Git and GitHub

---

## 📁 Project Structure

```
my-chatbot/
├── .streamlit/
│   ├── config.toml        # Dark theme settings
│   └── secrets.toml       # 🔐 API key (local only, never pushed)
├── .gitignore             # Keeps secrets out of GitHub
├── app.py                 # Main application logic
├── style.css              # Custom UI design
├── requirements.txt       # Python dependencies
├── screenshot.png         # App preview used in this README
└── README.md              # You are here
```

---

## 🚀 Run It Locally

**1. Clone the repository**
```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git
cd YOUR-REPO
```

**2. Create a virtual environment and install dependencies**
```bash
python -m venv venv
venv\Scripts\activate          # Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
```

**3. Add your API key**

Get a free key from [Google AI Studio](https://aistudio.google.com/), then create `.streamlit/secrets.toml`:
```toml
GEMINI_API_KEY = "your-api-key-here"
```

**4. Start the app**
```bash
streamlit run app.py
```
Open **http://localhost:8501** in your browser.

---

## ☁️ Deploy on Streamlit Cloud

1. Push this project to GitHub (the `.gitignore` already protects your key).
2. Go to [share.streamlit.io](https://share.streamlit.io/) and click **Create app**.
3. Select your repository, the `main` branch, and `app.py` as the main file.
4. Open **Advanced settings → Secrets** and paste:
   ```toml
   GEMINI_API_KEY = "your-api-key-here"
   ```
5. Click **Deploy**. Every `git push` updates the live app automatically.

---

## 🔐 Security

- The API key is stored only in `.streamlit/secrets.toml` locally and in the Streamlit Cloud Secrets box online.
- `secrets.toml` is listed in `.gitignore`, so it is **never uploaded** to GitHub.
- If a key is ever exposed, delete it in Google AI Studio and create a new one.

---

## 🧩 Troubleshooting

| Problem | Solution |
|---|---|
| `API key not found` | Check that the secret is named exactly `GEMINI_API_KEY` |
| `404 NOT_FOUND` | The model was retired, so choose another one from the dropdown |
| `429 RESOURCE_EXHAUSTED` | Free quota reached, so switch to a Flash model or try again later |
| Slow first response | Pro models think longer, so choose a Flash or Flash-Lite model |

---

## 🔮 Future Improvements

- 🔑 Password or login protection
- 📎 File and image upload
- 💾 Permanent chat history with a database
- 🌐 Multi-language interface
- 🎙️ Voice input and output

---

## 👨‍💻 Author

**Zeeshan Ahmad**

Built with ❤️ using Python, Streamlit, and Google Gemini.

---

<div align="center">

⭐ **If you like this project, give it a star on GitHub!** ⭐

**[🚀 Launch Nova AI](https://my-chatbot-804.streamlit.app/)**

</div>
