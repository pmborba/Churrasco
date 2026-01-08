import streamlit as st
import urllib.parse
from datetime import datetime

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Rachadinha Churrasco", page_icon="🍖")

# --- LINKS ---
# Foto do Fundo
fundo_url = "https://raw.githubusercontent.com/pmborba/Churrasco/main/WhatsApp%20Image%202026-01-08%20at%2014.55.05.jpeg"
# Playlist Bruno e Marrone
spotify_playlist = "https://open.spotify.com/embed/playlist/37i9dQZF1DZ06evO0QGq99?utm_source=generator"

# --- BANCO DE DADOS PIX ---
chaves_pix = {
    "Guy": "064.266.399-82",
    "Thi": "064.514.089-99",
    "Paulinho": "085.994.129-90"
}

# 2. ESTILO VISUAL (SEPARADO PARA NÃO DAR ERRO)
# Parte 1: CSS Estático (Sem aspas 'f' para evitar conflito com chaves)
st.markdown("""
    <style>
    /* Texto Branco e Sombras */
    h1, h2, h3, p, label, .stMarkdown, .stButton button, .stMetricLabel {
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
    /* Botão Calcular Verde */
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

# Parte 2: CSS Dinâmico (Apenas para o fundo)
st.markdown(f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("{fundo_url}");
        background-size: contain;
        background-repeat: no-repeat;
