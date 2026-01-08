import streamlit as st
import urllib.parse
from datetime import datetime

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Rachadinha Churrasco", page_icon="🍖")

# --- LINKS E DADOS ---
url_imagem = "https://raw.githubusercontent.com/pmborba/Churrasco/main/WhatsApp%20Image%202026-01-08%20at%2014.55.05.jpeg"

# Link do YouTube (Embed da Playlist Bruno & Marrone)
# O código abaixo pega o ID do vídeo e da playlist que você mandou
youtube_embed = "https://www.youtube.com/embed/98BMxJU1AGw?list=RDEMilQ9enpeArgd2xuJvt9ATw&autoplay=0"

pix_dict = {
    "Guy": "064.266.399-82",
    "Thi": "064.514.089-99",
    "Paulinho": "085.994.129-90"
}

# 2. ESTILO VISUAL (CSS PURO)
st.markdown("""
<style>
    /* Texto Branco e Sombras */
    h1, h2, h3, h4, h5, p, label, .stMarkdown, .stButton button, div[data-testid="stMetricValue"], span {
        color: white !important;
        text-shadow: 2px 2px 4px #000000;
    }
    /* Campos Transparente */
    .stCheckbox, div[data-baseweb="select"], .stNumberInput, .stTextArea textarea, .stTextInput input, .stSelectbox div, .stDateInput div {
        background-color: rgba(255, 255, 255, 0.3) !important;
        border-radius: 10px !important;
        color: black !important;
        font-weight: bold !important;
    }
    input, textarea {
        color: black !important;
        -webkit-text-fill-color: black !important;
    }
    /* Botão Verde */
    .stButton button {
        background-color: #25D366 !important;
        color: white !important;
        border: none;
        font-size: 20px;
        font-weight: bold;
        padding: 10px 24px;
        border-radius: 12px;
    }
    .stButton button:hover {
        border: 2px solid white;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. ESTILO DO FUNDO
css_fundo = """
<style>
.stApp {{
    background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("{url}");
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    background-attachment: fixed;
    background-color: #0e1117;
}}
</style>
""".format(url=url_imagem)
st.markdown(css_fundo, unsafe_allow_html=True)

# --- TÍTULO ---
st.title("🍖 Rachadinha dos amigos 🍖")

# --- PLAYER DO YOUTUBE (MODO SEGURO) ---
st.markdown("### 🎵 Som na Caixa")
# Iframe do YouTube
html_youtube = '<iframe width="100%" height="250" src="' + youtube_embed + '" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 12px;"></iframe>'
st.markdown(html_youtube, unsafe_allow_html=True)

# 4. CONFIGURAÇÃO
st.subheader("🏠 Configuração")
col_conf1, col_conf2 = st.columns([1.5, 1])
with col_conf1:
    host = st.selectbox("Quem é o anfitrião?", ["Guy", "Thi", "Paulinho"])
    chave_pix = pix_dict.get(host)
with col_conf2:
    data_sel = st.date_input("Data:", datetime.now())
    data_txt = data_sel.strftime("%d/%m/%Y")

# 5. PARTICIPANTES
st.subheader("👥 Quem participou?")
col_fam1, col_fam2 = st.columns(2)
with col_fam1:
    v_guy = st.checkbox("Família Guy", value=True)
    v_thi = st.checkbox("Família Thi", value=True)
with col_fam2:
    v_pau = st.checkbox("Família Paulinho", value=True)
    v_jor = st.checkbox("Jorge", value=True)

# 6. CONVIDADOS EXTRAS (LAYOUT PARA CELULAR)
st.markdown("---")
st.write("👤 **Convidados Extras**")

# Convidado 1
st.markdown("##### Convidado 1")
row1_c1, row1_c2 = st.columns([2, 1])
with row1_c1:
    nome1 = st.text_input("Nome:", key="n1", placeholder="Digite o nome...")
with row1_c2:
    tipo1 = st.selectbox("Cota:", ["Ninguém", "Individual", "Casal"], key="t1")

# Convidado 2
st.markdown("##### Convidado 2")
row2_c1, row2_c2 = st.columns([2, 1])
with row2_c1:
    nome2 = st.text_input("Nome:", key="n2", placeholder="Digite o nome...")
with row2_c2:
    tipo2 = st.selectbox("Cota:", ["Ninguém", "Individual", "Casal"], key="t2")

# LÓGICA DE CÁLCULO
num_cotas = 0
if v_guy: num_cotas += 2
if v_thi: num_cotas += 2
if v_pau: num_cotas += 2
if v_jor: num_cotas += 1

q1 = 0
if nome1 and tipo1 != "Ninguém":
    q1 = 1 if tipo1 == "Individual" else 2
    num_cotas += q1

q2 = 0
if nome2 and tipo2 != "Ninguém":
    q2 = 1 if tipo2 == "Individual" else 2
    num_cotas += q2

# 7. VALORES
st.markdown("---")
with st.expander("📝 CLIQUE AQUI PARA LANÇAR VALORES", expanded=True):
    lista_itens = ["Carne", "Pão de alho", "Linguiça", "Cerveja", "Jurupinga", "Vodka", "Fruta", "Carvão", "Gelo", "Outros"]
    cv1, cv2 = st.columns(2)
    dic_gastos = {}
    for i, item in enumerate(lista_itens):
        with cv1 if i % 2 == 0 else cv2:
            dic_gastos[item] = st.number_input(f"{item}", min_value=0.0, step=5.0, format="%.2f")

total = sum(dic_gastos.values())

# --- BOTÃO CALCULAR ---
if "estado_calc" not in st.session_state:
    st.session_state["estado_calc"] = False

st.markdown("<br>", unsafe_allow_html=True)
b1, b2, b3 = st.columns([1, 2, 1])
with b2:
    if st.button("CALCULAR 🚀", use_container_width=True):
        if total > 0:
            st.session_state["estado_calc"] = True
        else:
            st.warning("Preencha algum valor!")

# 8. RESULTADOS
if st.session_state["estado_calc"] and total > 0:
    st.divider()
    st.header(f"💰 Total Geral: R$ {total:.2f}")

    if num_cotas > 0:
        val_cota = total / num_cotas
        
        # Exibição Visual dos Resultados
        r1, r2 = st.columns(2)
        with r1:
            if v_guy: st.info(f"Família Guy: R$ {val_cota*2:.2f}")
            if v_thi: st.info(f"Família Thi: R$ {val_cota*2:.2f}")
            if q1 > 0: st.info(f"{nome1}: R$ {val_cota*q1:.2f}")
        with r2:
            if v_pau: st.info(f"Família Paulinho: R$ {val_cota*2:.2f}")
            if v_jor: st.info(f"Jorge: R$ {val_cota:.2f}")
            if q2 > 0: st.info(f"{nome2}: R$ {val_cota*q2:.2f}")

        # Montagem do Texto WhatsApp (Concatenação segura)
        msg = "🍖 *CHURRASCO DO " + host.upper() + "* 🍖\n"
        msg += "📅 Data: " + data_txt + "\n\n"
        msg += "💰 *Total: R$ " + "{:.2f}".format(total) + "*\n\n"
        
        if v_guy: msg += "👨‍👩‍👧‍👦 Família Guy: R$ " + "{:.2f}".format(val_cota*2) + "\n"
        if v_pau: msg += "👨‍👩‍👧‍👦 Família Paulinho: R$ " + "{:.2f}".format(val_cota*2) + "\n"
        if v_thi: msg += "👨‍👩‍👧‍👧 Família Thi: R$ " + "{:.2f}".format(val_cota*2) + "\n"
        if v_jor: msg += "❓ Jorge: R$ " + "{:.2f}".format(val_cota) + "\n"
        if q1 > 0: msg += "❓ " + nome1 + ": R$ " + "{:.2f}".format(val_cota*q1) + "\n"
        if q2 > 0: msg += "❓ " + nome2 + ": R$ " + "{:.2f}".format(val_cota*q2) + "\n"
        
        msg += "\n📍 *Pix para pagamento:* " + str(chave_pix)

        st.subheader("📲 Enviar Resumo")
        st.text_area("Copie o texto:", msg, height=250)
        
        # Botão Link Zap (HTML puro)
        link = "https://api.whatsapp.com/send?text=" + urllib.parse.quote(msg)
        
        html_botao = f"""
        <a href="{link}" target="_blank" style="text-decoration:none;">
            <div style="background-color:#25D366;color:white;padding:15px;text-align:center;border-radius:10px;font-weight:bold;font-size:18px;box-shadow:2px 2px 5px rgba(0,0,0,0.3);">
                🚀 ENVIAR PARA WHATSAPP
            </div>
        </a>
        """
        st.markdown(html_botao, unsafe_allow_html=True)

    else:
        st.error("Selecione os participantes!")
