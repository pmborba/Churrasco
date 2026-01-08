import streamlit as st
import urllib.parse
from datetime import datetime

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Rachadinha Churrasco", page_icon="🍖")

# --- LINKS (MÚSICA E FOTO) ---
fundo_url = "https://raw.githubusercontent.com/pmborba/Churrasco/main/WhatsApp%20Image%202026-01-08%20at%2014.55.05.jpeg"
musica_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-10.mp3" 

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
    /* Texto Branco */
    h1, h2, h3, p, label, .stMarkdown, .stButton button {{
        color: white !important;
        text-shadow: 2px 2px 4px #000000;
    }}
    /* Campos Transparente */
    .stCheckbox, div[data-baseweb="select"], .stNumberInput, .stTextArea textarea, .stTextInput input, .stSelectbox div, .stDateInput div {{
        background-color: rgba(255, 255, 255, 0.3) !important;
        border-radius: 10px !important;
        color: black !important;
        font-weight: bold !important;
    }}
    input, textarea {{
        color: black !important;
        -webkit-text-fill-color: black !important;
    }}
    /* Botão Calcular Verde */
    .stButton button {{
        background-color: #25D366 !important;
        color: white !important;
        border: none;
        font-size: 20px;
        font-weight: bold;
        padding: 10px 24px;
        border-radius: 12px;
    }}
    .stButton button:hover {{
        border: 2px solid white;
        color: white !important;
    }}
    .stAudio {{ margin-top: 20px; }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- BARRA LATERAL (MÚSICA) ---
with st.sidebar:
    st.header("🎵 Som na Caixa")
    st.audio(musica_url, format="audio/mp3")

# --- TÍTULO ---
st.title("🍖 Rachadinha dos amigos 🍖")

# 3. CONFIGURAÇÃO DO EVENTO
st.subheader("🏠 Configuração")
col_local, col_data = st.columns([1.5, 1])

with col_local:
    anfitriao = st.selectbox("Quem é o anfitrião?", ["Guy", "Thi", "Paulinho"])
    chave_final = chaves_pix.get(anfitriao)

with col_data:
    data_evento = st.date_input("Data:", datetime.now())
    data_str = data_evento.strftime("%d/%m/%Y")

# 4. PARTICIPANTES
st.subheader("👥 Quem participou?")
col_f1, col_f2 = st.columns(2)
with col_f1:
    v_guy = st.checkbox("Família Guy", value=True)
    v_thi = st.checkbox("Família Thi", value=True)
with col_f2:
    v_pau = st.checkbox("Família Paulinho", value=True)
    v_jor = st.checkbox("Jorge", value=True)

# 5. CONVIDADOS EXTRAS
st.markdown("---")
st.write("👤 **Convidados Extras**")
c1, c2 = st.columns([2, 1])
with c1:
    n1 = st.text_input("Nome Convidado 1", key="nome1", placeholder="Nome...")
    n2 = st.text_input("Nome Convidado 2", key="nome2", placeholder="Nome...")
with c2:
    t1 = st.selectbox("Cota 1", ["Ninguém", "Individual", "Casal"], key="tipo1")
    t2 = st.selectbox("Cota 2", ["Ninguém", "Individual", "Casal"], key="tipo2")

# LÓGICA DE COTAS
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

# 6. LANÇAMENTO DE VALORES
st.markdown("---")
with st.expander("📝 CLIQUE AQUI PARA LANÇAR OS VALORES (R$)", expanded=True):
    itens = ["Carne", "Pão de alho", "Linguiça", "Cerveja", "Jurupinga", "Vodka", "Fruta", "Carvão", "Gelo", "Outros"]
    col_v1, col_v2 = st.columns(2)
    v_gastos = {}

    for i, item in enumerate(itens):
        with col_v1 if i % 2 == 0 else col_v2:
            v_gastos[item] = st.number_input(f"{item}", min_value=0.0, step=5.0, format="%.2f")

total_geral = sum(v_gastos.values())

# --- CONTROLE DO BOTÃO CALCULAR ---
if "calcular" not in st.session_state:
    st.session_state["calcular"] = False

st.markdown("<br>", unsafe_allow_html=True)
col_b1, col_b2, col_b3 = st.columns([1, 2, 1])

with col_b2:
    if st.button("CALCULAR 🚀", use_container_width=True):
        if total_geral > 0:
            st.session_state["calcular"] = True
            st.balloons()
        else:
            st.warning("Preencha algum valor!")

# 7. EXIBIÇÃO DE RESULTADOS
if st.session_state["calcular"] and total_geral > 0:
    st.divider()
    st.header(f"💰 Total Geral: R$ {total_geral:.2f}")

    if total_cotas > 0:
        valor_cota = total_geral / total_cotas
        
        # Resultados Visuais
        r
