import streamlit as st
import urllib.parse
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="Rachadinha Churrasco", page_icon="🍖")

# Link da sua foto no GitHub
fundo_url = "https://raw.githubusercontent.com/pmborba/Churrasco/main/WhatsApp%20Image%202026-01-08%20at%2014.55.05.jpeg"

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
    
    /* Padronização dos textos */
    h1, h2, h3, p, label {{
        color: white !important;
        text-shadow: 2px 2px 4px #000000;
        font-family: 'sans-serif';
    }}

    /* Caixas de seleção e Inputs padronizados */
    .stCheckbox, div[data-baseweb="radio"], .stNumberInput, .stTextArea textarea {{
        background-color: rgba(255, 255, 255, 0.2) !important;
        border-radius: 10px !important;
        padding: 10px !important;
        margin-bottom: 10px !important;
    }}

    /* Fonte preta apenas onde há inserção de dados para contraste */
    input, textarea, span[data-baseweb="tag"] {{
        color: black !important;
        font-weight: bold !important;
    }}
    
    /* Ajuste para não sobrepor ícones de rádio */
    div[role="radiogroup"] {{
        gap: 15px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🍖 Rachadinha dos amigos")

# --- SELEÇÃO DE LOCAL ---
st.subheader("🏠 Onde é o churrasco?")
local_selecionado = st.selectbox(
    "Selecione o anfitrião:",
    ["Guy", "Thi", "Paulinho"]
)

# --- PARTICIPANTES (ORGANIZADOS EM COLUNAS IGUAIS) ---
st.subheader("👥 Quem participou?")
col1, col2 = st.columns(2)

with col1:
    vai_guy = st.checkbox("Família Guy", value=True)
    vai_thi = st.checkbox("Família Thi", value=True)
with col2:
    vai_paulinho = st.checkbox("Família Paulinho", value=True)
    vai_jorge = st.checkbox("Jorge", value=True)

# Lógica de Cotas
cotas = 0
lista_presentes = []
if vai_guy: cotas += 2; lista_presentes.append("Guy")
if vai_thi: cotas += 2; lista_presentes.append("Thi")
if vai_paulinho: cotas += 2; lista_presentes.append("Paulinho")
if vai_jorge: cotas += 1; lista_presentes.append("Jorge")

# --- GASTOS ---
st.subheader("📝 Lançar Valores")
itens = ["Carne", "Pão de alho", "Linguiça", "Cerveja", "Jurupinga", "Vodka", "Fruta", "Carvão", "Gelo", "Outros"]

# Organizando os campos de valores em 2 colunas para economizar espaço no celular
col_v1, col_v2 = st.columns(2)
gastos = {}

for i, item in enumerate(itens):
    with col_v1 if i % 2 == 0 else col_v2:
        gastos[item] = st.number_input(f"{item}", min_value=0.0, step=5.0, format="%.2f")

total = sum(gastos.values())

# --- RESULTADOS ---
if total > 0 and cotas > 0:
    valor_cota = total / cotas
    st.divider()
    st.metric("TOTAL GERAL", f"R$ {total:.2f}")

    # Exibição organizada
    res1, res2 = st.columns(2)
    with res1:
        if vai_guy: st.info(f"Família Guy: R$ {valor_cota*2:.2f}")
        if vai_thi: st.info(f"Família Thi: R$ {valor_cota*2:.2f}")
    with res2:
        if vai_paulinho: st.info(f"Família Paulinho: R$ {valor_cota*2:.2f}")
        if vai_jorge: st.success(f"Jorge: R$ {valor_cota:.2f}")

    # --- TEXTO WHATSAPP ---
    data = datetime.now().strftime("%d/%m/%Y")
    resumo = f"🍖 *CHURRASCO DO {local_selecionado.upper()}* 🍖\n📅 Data: {data}\n\n"
    resumo += f"💰 *Total: R$ {total:.2f}*\n\n"
    if vai_guy: resumo += f"🔹 Família Guy: R$ {valor_cota*2:.2f}\n"
    if vai_thi: resumo += f"🔹 Família Thi: R$ {valor_cota*2:.2f}\n"
    if vai_paulinho: resumo += f"🔹 Família Paulinho: R$ {valor_cota*2:.2f}\n"
    if vai_jorge: resumo += f"🔸 Jorge: R$ {valor_cota:.2f}\n"
    resumo += f"\n📍 Pix: SUA_CHAVE_AQUI"

    st.subheader("📲 Enviar Resumo")
    st.text_area("Confira o texto:", resumo, height=150)
    
    link_zap = f"https://api.whatsapp.com/send?text={urllib.parse.quote(resumo)}"
    
    st.markdown(f"""
        <a href="{link_zap}" target="_blank" style="text-decoration: none;">
            <div style="width: 100%; background-color: #25D366; color: white; padding: 15px; text-align: center; border-radius: 10px; font-weight: bold; font-size: 18px;">
                🚀 ENVIAR PARA WHATSAPP
            </div>
        </a>""", unsafe_allow_html=True)
