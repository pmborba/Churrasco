import streamlit as st
import urllib.parse
from datetime import datetime

# 1. Configuração inicial
st.set_page_config(page_title="Rachadinha Churrasco", page_icon="🍖")

# 2. Imagem de fundo
fundo_url = "https://raw.githubusercontent.com/pmborba/Churrasco/main/WhatsApp%20Image%202026-01-08%20at%2014.55.05.jpeg"

# 3. Banco de Dados Pix
chaves_pix = {
    "Guy": "064.266.399-82",
    "Thi": "064.514.089-99",
    "Paulinho": "085.994.129-90"
}

# 4. Estilo Visual (CSS)
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("{fundo_url}");
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        background-attachment: fixed;
        background-color: #0e1117;
    }}
    h1, h2, h3, p, label {{
        color: white !important;
        text-shadow: 2px 2px 4px #000000;
    }}
    .stCheckbox, div[data-baseweb="select"], .stNumberInput, .stTextArea textarea, .stTextInput input, .stSelectbox div {{
        background-color: rgba(255, 255, 255, 0.3) !important;
        border-radius: 10px !important;
        color: black !important;
        font-weight: bold !important;
    }}
    input, textarea {{
        color: black !important;
        -webkit-text-fill-color: black !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🍖 Rachadinha dos amigos 🍖")

# 5. Seleção de Anfitrião
st.subheader("🏠 Local do churras?")
anfitriao = st.selectbox("Quem é o anfitrião?", ["Guy", "Thi", "Paulinho"])
chave_final = chaves_pix.get(anfitriao)

# 6. Participantes Fixos
st.subheader("👥 Quem participou?")
col_f1, col_f2 = st.columns(2)
with col_f1:
    v_guy = st.checkbox("Família Guy", value=True)
    v_thi = st.checkbox("Família Thi", value=True)
with col_f2:
    v_pau = st.checkbox("Família Paulinho", value=True)
    v_jor = st.checkbox("Jorge", value=True)

# 7. Convidados Extras
st.markdown("---")
st.write("👤 **Convidados Extras**")
c_col1, c_col2 = st.columns([2, 1])
with c_col1:
    n1 = st.text_input("Nome Convidado 1", key="nome1")
    n2 = st.text_input("Nome Convidado 2", key="nome2")
with c_col2:
    t1 = st.selectbox("Cota 1", ["Ninguém", "Individual", "Casal"], key="tipo1")
    t2 = st.selectbox("Cota 2", ["Ninguém", "Individual", "Casal"], key="tipo2")

# 8. Lógica de Cotas
total_cotas = 0
if v_guy: total_cotas += 2
if v_thi: total_cotas += 2
if v_pau: total_cotas += 2
if v_jor: total_cotas += 1

val_c1 = 0
if n1 and t1 != "Ninguém":
    val_c1 = 1 if t1 == "Individual" else 2
    total_cotas += val_c1

val_c2 = 0
if n2 and t2 != "Ninguém":
    val_c2 = 1 if t2 == "Individual" else 2
    total_cotas += val_c2

# 9. Lançamento de Valores
st.subheader("📝 Lançar Valores")
