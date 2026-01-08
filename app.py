import streamlit as st
import urllib.parse
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="Rachadinha Churrasco", page_icon="🍖")

# Link da sua foto no GitHub
fundo_url = "https://raw.githubusercontent.com/pmborba/Churrasco/main/WhatsApp%20Image%202026-01-08%20at%2014.55.05.jpeg"

# --- BANCO DE DADOS DE CHAVES PIX ---
chaves_cadastradas = {
    "Guy": "Preencher a chave pix",
    "Thi": "Preencher a chave pix",
    "Paulinho": "085.994.129-90"
}

# --- ESTILO VISUAL ---
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
    .stCheckbox, div[data-baseweb="select"], .stNumberInput, .stTextArea textarea, .stTextInput input, .stSelectbox div {{
        background-color: rgba(255, 255, 255, 0.2) !important;
        border-radius: 10px !important;
        color: black !important;
        font-weight: bold !important;
    }}
    input {{ color: black !important; }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🍖 Rachadinha dos amigos 🍖")

# --- SELEÇÃO DE LOCAL E PIX ---
st.subheader("🏠 Local do churras?")
col_local, col_pix = st.columns([1, 1.5])
with col_local:
    local_selecionado = st.selectbox("Anfitrião:", ["Guy", "Thi", "Paulinho"])
with col_pix:
    chave_sugerida = chaves_cadastradas.get(local_selecionado, "")
    chave_pix = st.text_input("Confirmar Chave Pix:", value=chave_sugerida)

# --- PARTICIPANTES FIXOS ---
st.subheader("👥 Quem participou?")
col_f1, col_f2 = st.columns(2)
with col_f1:
    vai_guy = st.checkbox("Família Guy", value=True)
    vai_thi = st.checkbox("Família Thi", value=True)
with col_f2:
    vai_paulinho = st.checkbox("Família Paulinho", value=True)
    vai_jorge = st.checkbox("Jorge", value=True)

# --- CONVIDADOS EXTRAS ---
st.markdown("---")
st.write("👤 **Adicionar Convidados?**")

col_c1a, col_c1b = st.columns([2, 1])
with col_c1a:
    nome_c1 = st.text_input("Nome do convidado 1:", key="nc1")
with col_c1b:
    tipo_c1 = st.selectbox("Cota 1:", ["Ninguém", "Individual (1 cota)", "Casal (2 cotas)"], key="tc1")

col_c2a, col_c2b = st.columns([2, 1])
with col_c2a:
    nome_c2 = st.text_input("Nome do convidado 2:", key="nc2")
with col_c2b:
