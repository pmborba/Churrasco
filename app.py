import streamlit as st
import urllib.parse
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="Rachadinha Churrasco", page_icon="🍖")

# Link da sua foto no GitHub
fundo_url = "https://raw.githubusercontent.com/pmborba/Churrasco/main/WhatsApp%20Image%202026-01-08%20at%2014.55.05.jpeg"

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
    h1, h2, h3, p, label, .stMetric {{
        color: white !important;
        text-shadow: 2px 2px 4px #000000;
    }}
    /* Estilização para radio buttons, checkboxes e inputs */
    .stNumberInput div div, .stNumberInput button, .stTextArea textarea, [data-baseweb="radio"] div {{
        background-color: rgba(255, 255, 255, 0.3) !important;
        border: none !important;
        border-radius: 10px !important;
    }}
    input, textarea, span {{
        color: black !important;
        font-weight: bold !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🍖 Rachadinha dos amigos 🍖")

# --- SELEÇÃO DE LOCAL E DATA ---
data_atual = datetime.now().strftime("%d/%m/%Y")

st.subheader("🏠 Onde é o churrasco?")
local_selecionado = st.radio(
    "Selecione o anfitrião:",
    ["Guy", "Thi", "Paulinho"],
    horizontal=True
)

# --- SELEÇÃO DE PARTICIPANTES ---
st.subheader("👥 Quem participou?")
col_p1, col_p2 = st.columns(2)

with col_p1:
    vai_guy = st.checkbox("Família do Guy", value=True)
    vai_thi = st.checkbox("Família do Thi", value=True)
with col_p2:
    vai_paulinho = st.checkbox("Família do Paulinho", value=True)
    vai_jorge = st.checkbox("Jorge", value=True)

# Cálculo de Cotas
cotas_totais = 0
participantes_lista = []
if vai_guy: cotas_totais += 2; participantes_lista.append("Família Guy")
if vai_thi: cotas_totais += 2; participantes_lista.append("Família Thi")
if vai_paulinho: cotas_totais += 2; participantes_lista.append("Família Paulinho")
if vai_jorge: cotas_totais += 1; participantes_lista.append("Jorge")

# --- LANÇAMENTO DE GASTOS ---
itens = ["Carne", "Pão de alho", "Linguiça", "Cerveja", "Jurupinga", "Vodka", "Fruta", "Carvão", "Gelo", "Outros valores"]
gastos = {}

st.subheader("📝 Lançar Valores")
for item in itens:
    gastos[item] = st.number_input(f"{item} (R$)", min_value=0.0, value=0.0, step=5.0, format="%.2f")

total_geral = sum(gastos.values())

# --- RESULTADOS E ENVIO ---
if total_geral > 0 and cotas_totais > 0:
    cota_unitaria = total_geral / cotas_totais
    st.divider()
    st.header(f"Total: R$ {total_geral:.2f}")
    
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        if vai_guy: st.info(f"**Família Guy:** R$ {cota_unitaria * 2:.2f}")
        if vai_thi: st.info(f"**Família Thi:** R$ {cota_unitaria * 2:.2f}")
    with col_res2:
        if vai_paulinho: st.info(f"**Família Paulinho:** R$ {cota_unitaria * 2:.2f}")
        if vai_jorge: st.success(f"**Jorge:** R$ {cota_unitaria:.2f}")

    # --- FORMATANDO TEXTO PARA WHATSAPP ---
    # Título dinâmico conforme sua solicitação
    resumo_zap = f"🍖 *CHURRASCO DO {local_selecionado.upper()}* 🍖\n"
    resumo_zap += f"📅 Data: {data_atual}\n\n"
    resumo_zap += f"💰 Total: R$ {total_geral:.2f}\n"
    resumo_zap += f"👥 Participantes: {', '.join(participantes_lista)}\n\n"
    
    if vai_guy: resumo_zap += f"🔹 Família Guy: R$ {cota_unitaria*2:.2f}\n"
    if vai_thi: resumo_zap += f"🔹 Família Thi: R$ {cota_unitaria*2:.2f}\n"
    if vai_paulinho: resumo_zap += f"🔹 Família Paulinho: R$ {cota_unitaria*2:.2f}\n"
    if vai_jorge: resumo_zap += f"🔸 Jorge: R$ {cota_unitaria:.2f}\n"
    
    resumo_zap += f"\n📍 Pix: SUA_CHAVE_AQUI"

    texto_para_url = urllib.parse.quote(resumo_zap)
    link_whatsapp = f"https://api.whatsapp.com/send?text={texto_para_url}"

    st.subheader("📲 Enviar para o Grupo")
    st.text_area("Texto que será enviado:", value=resumo_zap, height=220)
    
    st.markdown(
        f"""
        <a href="{link_whatsapp}" target="_blank" style="text-decoration: none;">
            <div style="width: 100%; background-color: #25D366; color: white; padding: 15px; text-align: center; border-radius: 10px; font-weight: bold; font-size: 18px; box-shadow: 2px 2px 5px rgba(0,0,0,0.3);">
                🚀 ENVIAR PARA O WHATSAPP
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )
elif total_geral > 0 and cotas_totais == 0:
    st.error("Selecione quem participou para dividir a conta!")
else:
    st.write("Aguardando lançamento de valores...")
