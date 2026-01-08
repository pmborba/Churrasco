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

# 4. Estilo Visual (CSS) - Foto Centralizada
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
itens = ["Carne", "Pão de alho", "Linguiça", "Cerveja", "Jurupinga", "Vodka", "Fruta", "Carvão", "Gelo", "Outros"]
col_v1, col_v2 = st.columns(2)
v_gastos = {}

for i, item in enumerate(itens):
    with col_v1 if i % 2 == 0 else col_v2:
        v_gastos[item] = st.number_input(f"{item}", min_value=0.0, step=5.0, format="%.2f")

total_geral = sum(v_gastos.values())

# 10. BLOCO DE RESULTADOS
if total_geral > 0:
    st.divider()
    st.header(f"Total Geral: R$ {total_geral:.2f}")
    
    if total_cotas > 0:
        valor_cota = total_geral / total_cotas
        
        # Blocos de resultado azuis
        res1, res2 = st.columns(2)
        with res1:
            if v_guy: st.info(f"Família Guy: R$ {valor_cota*2:.2f}")
            if v_thi: st.info(f"Família Thi: R$ {valor_cota*2:.2f}")
            if val_c1 > 0: st.info(f"{n1}: R$ {valor_cota*val_c1:.2f}")
        with res2:
            if v_pau: st.info(f"Família Paulinho: R$ {valor_cota*2:.2f}")
            if v_jor: st.info(f"Jorge: R$ {valor_cota:.2f}")
            if val_c2 > 0: st.info(f"{n2}: R$ {valor_cota*val_c2:.2f}")

        # Texto para WhatsApp (Sintaxe rigorosa para evitar erros)
        hoje = datetime.now().strftime("%d/%m/%Y")
        resumo = "🍖 *CHURRASCO DO " + anfitriao.upper() + "* 🍖\n"
        resumo += "📅 Data: " + hoje + "\n\n"
        resumo += "💰 *Total: R$ " + "{:.2f}".format(total_geral) + "*\n\n"
        
        if v_guy: resumo += "👨‍👩‍👧‍👦 Família Guy: R$ " + "{:.2f}".format(valor_cota*2) + "\n"
        if v_pau: resumo += "👨‍👩‍👧‍👦 Família Paulinho: R$ " + "{:.2f}".format(valor_cota*2) + "\n"
        if v_thi: resumo += "👨‍👩‍👧‍👧 Família Thi: R$ " + "{:.2f}".format(valor_cota*2)
