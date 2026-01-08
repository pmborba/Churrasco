import streamlit as st
import urllib.parse
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="Rachadinha Churrasco", page_icon="🍖")

# Link da sua foto no GitHub
fundo_url = "https://raw.githubusercontent.com/pmborba/Churrasco/main/WhatsApp%20Image%202026-01-08%20at%2014.55.05.jpeg"

# --- BANCO DE DADOS DE CHAVES PIX ---
chaves_cadastradas = {
    "Guy": "064.266.399-82",
    "Thi": "064.514.089-99",
    "Paulinho": "085.994.129-90"
}

# --- ESTILO VISUAL ---
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

# --- SELEÇÃO DE LOCAL ---
st.subheader("🏠 Local do churras?")
local_selecionado = st.selectbox("Anfitrião:", ["Guy", "Thi", "Paulinho"])
chave_pix_final = chaves_cadastradas.get(local_selecionado, "")

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
    tipo_c2 = st.selectbox("Cota 2:", ["Ninguém", "Individual (1 cota)", "Casal (2 cotas)"], key="tc2")

# Lógica de Cotas
cotas_calc = 0
if vai_guy: cotas_calc += 2
if vai_thi: cotas_calc += 2
if vai_paulinho: cotas_calc += 2
if vai_jorge: cotas_calc += 1

c1_cota = 0
if nome_c1 and tipo_c1 != "Ninguém":
    c1_cota = 1 if "Individual" in tipo_c1 else 2
    cotas_calc += c1_cota

c2_cota = 0
if nome_c2 and tipo_c2 != "Ninguém":
    c2_cota = 1 if "Individual" in tipo_c2 else 2
    cotas_calc += c2_cota

# --- LANÇAMENTO DE GASTOS ---
st.subheader("📝 Lançar Valores")
itens_lista = ["Carne", "Pão de alho", "Linguiça", "Cerveja", "Jurupinga", "Vodka", "Fruta", "Carvão", "Gelo", "Outros"]
col_v1, col_v2 = st.columns(2)
gastos_dict = {}

for idx, item_nome in enumerate(itens_lista):
    with col_v1 if idx % 2 == 0 else col_v2:
        gastos_dict[item_nome] = st.number_input(f"{item_nome}", min_value=0.0, step=5.0, format="%.2f")

total_valor = sum(gastos_dict.values())

# --- EXIBIÇÃO DO RESUMO ---
# O bloco só aparece se o total for maior que zero
if total_valor > 0:
    st.divider()
    st.header(f"Total Geral: R$ {total_valor:.2f}")
    
    if cotas_calc > 0:
        v_cota = total_valor / cotas_calc
        
        # Blocos de resultado az
