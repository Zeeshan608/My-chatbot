from pathlib import Path

import streamlit as st
from google import genai
from google.genai import types

# ---------- Page setup ----------
st.set_page_config(
    page_title="Nova AI Assistant",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="expanded",
)

css = Path(__file__).parent / "style.css"
st.markdown(f"<style>{css.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)

# ---------- Secure API key (never hardcoded) ----------
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    st.error(
        "API key not found. Add GEMINI_API_KEY to `.streamlit/secrets.toml` (local) "
        "or to the Secrets box in Streamlit Cloud."
    )
    st.stop()

client = genai.Client(api_key=api_key)

# ---------- Config ----------
FALLBACK_MODELS = ["gemini-3-flash-preview", "gemini-3.1-pro-preview"]
SKIP = ("tts", "image", "live", "audio", "embedding", "transcribe", "translate",
        "omni", "robotics", "lyria", "veo", "imagen", "aqa", "learnlm", "gemma")


@st.cache_data(ttl=3600, show_spinner=False)
def get_models(_client):
    """Ask Google which chat models this API key can use right now."""
    try:
        names = []
        for m in _client.models.list():
            actions = getattr(m, "supported_actions", None) or []
            name = (m.name or "").replace("models/", "")
            if "generateContent" in actions and name.startswith("gemini") \
                    and not any(k in name for k in SKIP):
                names.append(name)
        return sorted(set(names), reverse=True) or FALLBACK_MODELS
    except Exception:
        return FALLBACK_MODELS


MODELS = get_models(client)
PERSONAS = {
    "General Assistant": "You are a helpful, friendly and concise assistant.",
    "Professional Writer": "You are an expert writer. Produce polished, well-structured text.",
    "Coding Mentor": "You are a patient senior developer. Explain clearly and give working code.",
    "Study Tutor": "You are a tutor. Explain step by step using simple examples.",
}
SUGGESTIONS = [
    ("📝 Write an email", "Write a professional email asking for a project deadline extension."),
    ("💡 Explain a concept", "Explain how large language models work in simple terms."),
    ("🐍 Python help", "Show me a Python function that reads a CSV file and summarizes it."),
    ("🚀 Business ideas", "Give me 5 startup ideas I can build using AI."),
]

# ---------- State ----------
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pending" not in st.session_state:
    st.session_state.pending = None

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown('<div class="side-title">✨ Nova AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="side-sub">Powered by Google Gemini</div>', unsafe_allow_html=True)

    persona = st.selectbox("Persona", list(PERSONAS.keys()))
    model = st.selectbox("Model", MODELS)
    temperature = st.slider("Creativity", 0.0, 1.5, 0.7, 0.1)

    st.divider()
    if st.button("🗑️ New chat"):
        st.session_state.messages = []
        st.rerun()

    if st.session_state.messages:
        transcript = "\n\n".join(
            f"{m['role'].upper()}: {m['content']}" for m in st.session_state.messages
        )
        st.download_button("⬇️ Download chat", transcript, "chat.txt", use_container_width=True)

    st.caption(f"💬 {len(st.session_state.messages)} messages")

# ---------- Header ----------
if not st.session_state.messages:
    st.markdown(
        """
        <div class="hero">
          <span class="badge">● ONLINE · GEMINI POWERED</span>
          <h1>Hello, I'm Nova</h1>
          <p>Your smart AI assistant. Ask anything, or pick a quick start below.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    cols = st.columns(2)
    for i, (label, text) in enumerate(SUGGESTIONS):
        if cols[i % 2].button(label, key=f"s{i}"):
            st.session_state.pending = text
            st.rerun()
else:
    st.markdown('<div class="mini-header">✨ Nova AI</div>', unsafe_allow_html=True)

# ---------- Render history ----------
for m in st.session_state.messages:
    with st.chat_message(m["role"], avatar="🧑" if m["role"] == "user" else "✨"):
        st.markdown(m["content"])


def to_contents(messages):
    return [
        types.Content(
            role="model" if m["role"] == "assistant" else "user",
            parts=[types.Part(text=m["content"])],
        )
        for m in messages
    ]


# ---------- Handle input ----------
prompt = st.chat_input("Message Nova...")
if st.session_state.pending:
    prompt = st.session_state.pending
    st.session_state.pending = None

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="✨"):
        placeholder = st.empty()
        full = ""
        try:
            with st.spinner("Thinking..."):
                stream = client.models.generate_content_stream(
                    model=model,
                    contents=to_contents(st.session_state.messages),
                    config=types.GenerateContentConfig(
                        system_instruction=PERSONAS[persona],
                        temperature=temperature,
                        max_output_tokens=2000,
                    ),
                )
                for chunk in stream:
                    if chunk.text:
                        full += chunk.text
                        placeholder.markdown(full + "▌")
            placeholder.markdown(full)
        except Exception as e:
            placeholder.error(f"Error: {e}")
            st.session_state.messages.pop()
            st.stop()

    st.session_state.messages.append({"role": "assistant", "content": full})
    st.rerun()

st.markdown('<div class="footer">Built with Streamlit & Google Gemini</div>', unsafe_allow_html=True)
