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

# --- ESTILO VISUAL RESTAURADO ---
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
    /* Estilo para a exibição da chave Pix fixa */
    .pix-box {{
        background-color: rgba(255, 255, 255, 0.3);
        padding: 10px;
        border-radius: 10px;
        color: black;
        font-weight: bold;
        text-align: center;
        margin-top: 5px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🍖 Rachadinha dos amigos 🍖")

# --- SELEÇÃO DE LOCAL E VÍNCULO DE PIX ---
st.subheader("🏠 Local do churras?")
col_local, col_pix_info = st.columns([1, 1.5])

with col_local:
    local_selecionado = st.selectbox("Anfitrião:", ["Guy", "Thi", "Paulinho"])

with col_pix_info:
    # Apenas exibe a chave vinculada ao anfitrião
    chave_pix = chaves_cadastradas.get(local_selecionado, "")
    st.markdown(f'<p style="margin-bottom: 0px;">Pix para Pagamento:</p><div class="pix-box">{chave_pix}</div>', unsafe_allow_html=True)

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

# Lógica de Contagem de Cotas
cotas = 0
if vai_guy: cotas += 2
if vai_thi: cotas += 2
if vai_paulinho: cotas += 2
if vai_jorge: cotas += 1

c1_val = 0
if nome_c1 and tipo_c1 != "Ninguém":
    c1_val = 1 if "Individual" in tipo_c1 else 2
    cotas += c1_val

c2_val = 0
if nome_c2 and tipo_c2 != "Ninguém":
    c2_val = 1 if "Individual" in tipo_c2 else 2
    cotas += c2_val

# --- LANÇAMENTO DE GASTOS ---
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
        if c1_val > 0: st.info(f"{nome_c1}: R$ {valor_cota * c1_val:.2f}")
    with res2:
        if vai_paulinho: st.info(f"Família Paulinho: R$ {valor_cota*2:.2f}")
        if vai_jorge: st.info(f"Jorge: R$ {valor_cota:.2f}")
        if c2_val > 0: st.info(f"{nome_c2}: R$ {valor_cota * c2_val:.2f}")

    # --- TEXTO WHATSAPP ---
    data = datetime.now().strftime("%d/%m/%Y")
    resumo = f"🍖 *CHURRASCO DO {local_selecionado.upper()}* 🍖\n📅 Data: {data}\n\n"
    resumo += f"💰 *Total: R$ {total:.2f}*\n\n"
    
    if vai_guy: resumo += f"👨‍👩‍👧‍👦 Família Guy: R$ {valor_cota*2:.2f}\n"
    if vai_paulinho: resumo += f"👨‍👩‍👧‍👦 Família Paulinho: R$ {valor_cota*2:.2f}\n"
    if vai_thi: resumo += f"👨‍👩‍👧‍👧 Família Thi: R$ {valor_cota*2:.2f}\n"
    if vai_jorge: resumo += f"❓ Jorge: R$ {valor_cota:.2f}\n"
    
    if c1_val > 0: resumo += f"❓ {nome_c1}: R$ {valor_cota * c1_val:.2f}\n"
    if c2_val > 0: resumo += f"❓ {nome_c2}: R$ {valor_cota * c2_val:.2f}\n"
    
    resumo += f"\n📍 *Pix para pagamento:*\n{chave_pix}"

    st.subheader("📲 Enviar Resumo")
    st.text_area("Confira o texto:", resumo, height=250)
    
    link_zap = f"https://api.whatsapp.com/send?text={urllib.parse.quote(resumo)}"
    
    st.markdown(f"""
        <a href="{link_zap}" target="_blank" style="text-decoration: none;">
            <div style="width: 100%; background-color: #25D366; color: white; padding: 15px; text-align: center; border-radius: 10px; font-weight: bold; font-size: 18px; box-shadow: 2px 2px 5px rgba(0,0,0,0.3);">
                🚀 ENVIAR PARA WHATSAPP
            </div>
        </a>""", unsafe_allow_html=True)
else:
    st.write("Aguardando lançamento de valores...")
