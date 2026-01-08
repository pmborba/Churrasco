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
    
    h1, h2, h3, p, label {{
        color: white !important;
        text-shadow: 2px 2px 4px #000000;
    }}

    /* Caixas de seleção, Inputs e Chave Pix */
    .stCheckbox, div[data-baseweb="select"], .stNumberInput, .stTextArea textarea, .stTextInput input {{
        background-color: rgba(255, 255, 255, 0.2) !important;
        border-radius: 10px !important;
        color: black !important;
        font-weight: bold !important;
    }}

    /* Ajuste específico para o campo de texto da chave Pix */
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

# --- SELEÇÃO DE LOCAL E PIX ---
st.subheader("🏠 Onde é o churrasco?")
col_local, col_pix = st.columns([1, 1.5])

with col_local:
    local_selecionado = st.selectbox("Anfitrião:", ["Guy", "Thi", "Paulinho"])

with col_pix:
    chave_pix = st.text_input("Chave Pix para pgto:", placeholder="Celular, CPF ou Aleatória")

# --- PARTICIPANTES ---
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
if vai_guy: cotas += 2
if vai_thi: cotas += 2
if vai_paulinho: cotas += 2
if vai_jorge: cotas += 1

# --- GASTOS ---
st.subheader("📝 Lançar Valores")
itens = ["Carne", "Pão de alho", "Linguiça", "Cerveja", "Jurupinga", "Vodka", "Fruta", "Carvão", "Gelo", "Outros"]

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
    
    if chave_pix:
        resumo += f"\n📍 *Pix para pagamento:*\n{chave_pix}"
    else:
        resumo += f"\n📍 *Pix para pagamento:* (Combinar no grupo)"

    st.subheader("📲 Enviar Resumo")
    st.text_area("Confira o texto:", resumo, height=200)
    
    link_zap = f"https://api.whatsapp.com/send?text={urllib.parse.quote(resumo)}"
    
    st.markdown(f"""
        <a href="{link_zap}" target="_blank" style="text-decoration: none;">
            <div style="width: 100%; background-color: #25D366; color: white; padding: 15px; text-align: center; border-radius: 10px; font-weight: bold; font-size: 18px; box-shadow: 2px 2px 5px rgba(0,0,0,0.3);">
                🚀 ENVIAR PARA WHATSAPP
            </div>
        </a>""", unsafe_allow_html=True)
elif total > 0 and cotas == 0:
    st.error("Selecione quem participou!")
else:
    st.write("Aguardando lançamento de valores...")
