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

# --- ESTILO VISUAL (FOTO CENTRALIZADA E TRANSPARÊNCIA) ---
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
chave_pix_atual = chaves_cadastradas.get(local_selecionado, "")

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

# Lógica de Cotagem de Cotas
cotas_totais = 0
if vai_guy: cotas_totais += 2
if vai_thi: cotas_totais += 2
if vai_paulinho: cotas_totais += 2
if vai_jorge: cotas_totais += 1

# Processamento Convidados
c1_qtd = 0
if nome_c1 and "Ninguém" not in tipo_c1:
    c1_qtd = 1 if "Individual" in tipo_c1 else 2
    cotas_totais += c1_qtd

c2_qtd = 0
if nome_c2 and "Ninguém" not in tipo_c2:
    c2_qtd = 1 if "Individual" in tipo_c2 else 2
    cotas_totais += c2_qtd

# --- LANÇAMENTO DE GASTOS ---
st.subheader("📝 Lançar Valores")
itens = ["Carne", "Pão de alho", "Linguiça", "Cerveja", "Jurupinga", "Vodka", "Fruta", "Carvão", "Gelo", "Outros"]
col_v1, col_v2 = st.columns(2)
gastos = {}

for idx, item in enumerate(itens):
    with col_v1 if idx % 2 == 0 else col_v2:
        gastos[item] = st.number_input(f"{item}", min_value=0.0, step=5.0, format="%.2f")

total_geral = sum(gastos.values())

# --- BLOCO FINAL DE RESUMO (SÓ APARECE SE TIVER VALOR) ---
if total_geral > 0:
    st.divider()
    st.header(f"Total Geral: R$ {total_geral:.2f}")
    
    if cotas_totais > 0:
        v_por_cota = total_geral / cotas_totais
        
        # Resultados em boxes azuis
        res_col1, res_col2 = st.columns(2)
        with res_col1:
            if vai_guy: st.info(f"Família Guy: R$ {v_por_cota*2:.2f}")
            if vai_thi: st.info(f"Família Thi: R$ {v_por_cota*2:.2f}")
            if c1_qtd > 0: st.info(f"{nome_c1}: R$ {v_por_cota * c1_qtd:.2f}")
        with res_col2:
            if vai_paulinho: st.info(f"Família Paulinho: R$ {v_por_cota*2:.2f}")
            if vai_jorge: st.info(f"Jorge: R$ {v_por_cota:.2f}")
            if c2_qtd > 0: st.info(f"{nome_c2}: R$ {v_por_cota * c2_qtd:.2f}")

        # --- PREPARAÇÃO DA MENSAGEM WHATSAPP ---
        hoje = datetime.now().strftime("%d/%m/%Y")
        resumo_texto = f"🍖 *CHURRASCO DO {local_selecionado.upper()}* 🍖\n📅 Data: {hoje}\n\n"
        resumo_texto += f"💰 *Total: R$ {total_geral:.2f}*\
