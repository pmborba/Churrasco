import streamlit as st
import urllib.parse
from datetime import datetime

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Rachadinha Churrasco", page_icon="🍖")

# --- LINKS ---
fundo_url = "https://raw.githubusercontent.com/pmborba/Churrasco/main/WhatsApp%20Image%202026-01-08%20at%2014.55.05.jpeg"

# --- BANCO DE DADOS PIX ---
chaves_pix = {
    "Guy": "064.266.399-82",
    "Thi": "064.514.089-99",
    "Paulinho": "085.994.129-90"
}

# 2. ESTILO VISUAL (CSS)
st.markdown(
    f"""
    <style>
    /* Fundo Centralizado */
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("{fundo_url}");
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        background-attachment: fixed;
        background-color: #0e1117;
    }}
    /* Texto Branco e Sombras */
    h1, h2, h3, p, label, .stMarkdown, .stButton button, .stMetricLabel {{
        color: white !important;
        text-shadow: 2px 2px 4px #000000;
    }}
    /* Campos Transparente */
    .stCheckbox, div[data-baseweb="select"], .stNumberInput, .stTextArea textarea, .stTextInput input, .stSelectbox div, .stDateInput div {{
        background-color: rgba(255, 255, 255, 0.3) !important;
