import streamlit as st
import urllib.parse
from datetime import datetime

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Rachadinha Churrasco", page_icon="🍖")

# --- LINKS ---
url_imagem = "https://raw.githubusercontent.com/pmborba/Churrasco/main/WhatsApp%20Image%202026-01-08%20at%2014.55.05.jpeg"
# Link "Embed" oficial do Spotify (Bruno & Marrone)
url_spotify = "https://open.spotify.com/embed/playlist/37i9dQZF1DZ06evO1nK5lE?utm_source=generator"

# --- DADOS PIX ---
pix_dict = {
    "Guy": "064.266.399-82",
    "Thi": "064.514.089-99",
    "Paulinho": "085.994.129-90"
}

# 2. ESTILO VISUAL (CSS BLINDADO)
st.markdown("""
<style>
    /* Texto Branco */
    h1, h2, h3, p, label, .stMarkdown, .stButton button, div[data-testid="stMetricValue"] {
        color: white !important;
        text-shadow: 2px 2px 4px #000000;
    }
    /* Campos Transparente */
    .stCheckbox, div[data-baseweb="select"], .stNumberInput, .stTextArea textarea, .stTextInput input, .stSelectbox div, .stDateInput div {
        background-color: rgba(255, 255, 255, 0.3) !important;
        border-radius: 10px !important;
        color: black !important;
        font-weight: bold !important;
    }
    input, textarea {
        color: black !important;
        -webkit-text-fill-color: black !important;
    }
    /* Botão Verde */
    .stButton button {
        background-color: #25D366 !important;
        color: white !important;
        border: none;
        font-size: 20px;
        font-weight: bold;
        padding: 10px 24px;
        border-radius: 12px;
    }
    .stButton button:hover {
        border: 2px solid white;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# CSS do Fundo (Separado para não dar erro de aspas)
css_fundo = f"""
<style>
.stApp {{
    background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("{url_imagem}");
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    background-attachment: fixed;
    background-color: #0e1117;
}}
</style>
"""
st.markdown(css_fundo, unsafe_allow_html=True)

# --- BARRA LATERAL (SPOTIFY VISUAL) ---
with st.sidebar:
    st.header("🎵 Modão Sertanejo")
    # Player Embutido (Iframe)
    html_spotify = f'<iframe style="border-radius
