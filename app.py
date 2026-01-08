import streamlit as st
import urllib.parse
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="Rachadinha Churrasco", page_icon="🍖")

# Link da sua foto no GitHub
fundo_url = "https://raw.githubusercontent.com/pmborba/Churrasco/main/WhatsApp%20Image%202026-01-08%20at%2014.55.05.jpeg"

# --- BANCO DE DADOS DE CHAVES PIX ---
# TODO: Substitua os textos abaixo pelas chaves reais
chaves_cadastradas = {
    "Guy": "CHAVE_DO_GUY",
    "Thi": "CHAVE_DO_THI",
    "Paulinho": "CHAVE_DO_PAULINHO"
}

# --- ESTILO VISUAL PADRONIZADO ---
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url("{fundo_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    h1, h2, h3, p, label {{
        color: white !important;
        text-shadow: 2px 2px 4px #000000;
    }}
    .stCheckbox, div[data-baseweb="select"], .stNumberInput, .stTextArea textarea, .stTextInput input {{
        background-color: rgba(255, 255, 255, 0.2) !important;
        border-radius: 10px !important;
        color: black !important;
        font-weight: bold !important;
    }}
    .stTextInput div div {{
        background-color: rgba(255, 255, 255, 0.3) !important;
        border-radius: 10px !important;
    }}
    input {{
        color: black !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🍖 Rachadinha dos amigos")

# --- SELEÇÃO DE LOCAL E PIX AUTOMÁTICO ---
st.subheader("🏠 Onde é o churrasco?")
col_local, col_pix = st.columns([1, 1.5])

with col_local:
    local_selecionado = st.selectbox("Anfitrião:", ["Guy", "Thi", "Paulinho"])

with col_pix:
    # O campo de Pix agora puxa o valor do dicionário baseado no local selecionado
