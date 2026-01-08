import streamlit as st
import urllib.parse
from datetime import datetime

# 1. Configuração da página
st.set_page_config(page_title="Rachadinha Churrasco", page_icon="🍖")

# 2. Link da imagem de fundo
fundo_url = "https://raw.githubusercontent.com/pmborba/Churrasco/main/WhatsApp%20Image%202026-01-08%20at%2014.55.05.jpeg"

# 3. Banco de Dados Pix
chaves_pix = {
    "Guy": "064.266.399-82",
    "Thi": "064.514.089-99",
    "Paulinho": "085.994.129-90"
}

# 4. Estilo Visual (CSS) - Foto Centralizada e Transparência
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
    nome_c1 = st.text_input("Nome Convidado 1", key="n1")
    nome_c2 = st.text_input("Nome Convidado 2", key="n2")
with c_col2:
    tipo_c1 = st.selectbox("Cota 1", ["Ninguém", "Individual", "Casal"], key="t1")
    tipo_c2 = st.selectbox("Cota 2", ["Ninguém", "Individual", "Casal"], key="t2")

# 8. Lógica de Cotas
total_cotas = 0
if v_guy: total_cotas += 2
if v_thi: total_cotas += 2
if v_pau: total_cotas += 2
if v_jor: total_cotas += 1

qtd_c1 = 0
if nome_c1 and tipo_c1 != "Ninguém":
    qtd_c1 = 1 if tipo_c1 == "Individual" else 2
    total_cotas += qtd_c1

qtd_c2 = 0
if nome_c2 and tipo_c2 != "Ninguém":
    qtd_c2 = 1 if tipo_c2 == "Individual" else 2
    total_cotas += qtd_c2

# 9. Lançamento de Valores
st.subheader("📝 Lançar Valores")
itens = ["Carne", "Pão de alho", "Linguiça", "Cerveja", "Jurupinga", "Vodka", "Fruta", "Carvão", "Gelo", "Outros"]
col_v1, col_v2 = st.columns(2)
v_gastos = {}

for i, item in enumerate(itens):
    with col_v1 if i % 2 == 0 else col_v2:
        v_gastos[item] = st.number_input(f"{item}", min_value=0.0, step=5.0, format="%.2f")

total_geral = sum(v_gastos.values())

# 10. BLOCO DE RESULTADOS (Só aparece se houver valor)
if total_geral > 0:
    st.divider()
    st.header(f"Total: R$ {total_geral:.2f}")
    
    if total_cotas > 0:
        valor_cota = total_geral / total_cotas
        
        # Blocos Azuis
        res1, res2 = st.columns(2)
        with res1:
            if v_guy: st.info(f"Família Guy: R$ {valor_cota*2:.2f}")
            if v_thi: st.info(f"Família Thi: R$ {valor_cota*2:.2f}")
            if qtd_c1 > 0: st.info(f"{nome_c1}: R$ {valor_cota*qtd_c1:.2f}")
        with res2:
            if v_pau: st.info(f"Família Paulinho: R$ {valor_cota*2:.2f}")
            if v_jor: st.info(f"Jorge: R$ {valor_cota:.2f}")
            if qtd_c2 > 0: st.info(f"{nome_c2}: R$ {valor_cota*qtd_c2:.2f}")

        # Texto para WhatsApp
        hoje = datetime.now().strftime("%d/%m/%Y")
        resumo = f"🍖 *CHURRASCO DO {anfitriao.upper()}* 🍖\n📅 Data: {hoje}\n\n"
        resumo += f"💰 *Total: R$ {total_geral:.2f}*\n\n"
        
        if v_guy: resumo += f"👨‍👩‍👧‍👦 Família Guy: R$ {valor_cota*2:.2f}\n
