import streamlit as st
import urllib.parse
from datetime import datetime

# 1. Configuração inicial
st.set_page_config(page_title="Rachadinha Churrasco", page_icon="🍖")

# --- LINKS DE MÍDIA ---
fundo_url = "https://raw.githubusercontent.com/pmborba/Churrasco/main/WhatsApp%20Image%202026-01-08%20at%2014.55.05.jpeg"
musica_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-10.mp3" 

# --- BANCO DE DADOS DE CHAVES PIX ---
chaves_pix = {
    "Guy": "064.266.399-82",
    "Thi": "064.514.089-99",
    "Paulinho": "085.994.129-90"
}

# --- ESTILO VISUAL (CSS) ---
st.markdown(
    f"""
    <style>
    /* Fundo com Foto Centralizada */
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("{fundo_url}");
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        background-attachment: fixed;
        background-color: #0e1117;
    }}
    /* Textos em Branco */
    h1, h2, h3, p, label, .stMarkdown, .stButton button {{
        color: white !important;
        text-shadow: 2px 2px 4px #000000;
    }}
    /* Campos de Dados com Transparência */
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
    /* Estilo do Botão Calcular */
    .stButton button {{
        background-color: #25D366 !important;
        color: white !important;
        border: none;
        font-size: 20px;
        font-weight: bold;
        padding: 10px 24px;
        border-radius: 12px;
        transition-duration: 0.4s;
    }}
    .stButton button:hover {{
        background-color: #128C7E !important;
        color: white !important;
        border: 2px solid white;
    }}
    .stAudio {{ margin-top: 20px; }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- SIDEBAR (Música) ---
with st.sidebar:
    st.header("🎵 Som na Caixa")
    st.audio(musica_url, format="audio/mp3")
    st.info("Dica: Dê o play para animar o churrasco!")

# --- TÍTULO ---
st.title("🍖 Rachadinha dos amigos 🍖")

# 2. Configurações do Evento
st.subheader("🏠 Configuração do Evento")
col_local, col_data = st.columns([1.5, 1])

with col_local:
    anfitriao = st.selectbox("Quem é o anfitrião?", ["Guy", "Thi", "Paulinho"])
    chave_final = chaves_pix.get(anfitriao)

with col_data:
    data_evento = st.date_input("Data:", datetime.now())
    data_formatada = data_evento.strftime("%d/%m/%Y")

# 3. Participantes Fixos
st.subheader("👥 Quem participou?")
col_f1, col_f2 = st.columns(2)
with col_f1:
    v_guy = st.checkbox("Família Guy", value=True)
    v_thi = st.checkbox("Família Thi", value=True)
with col_f2:
    v_pau = st.checkbox("Família Paulinho", value=True)
    v_jor = st.checkbox("Jorge", value=True)

# 4. Convidados Extras
st.markdown("---")
st.write("👤 **Convidados Extras**")
c_col1, c_col2 = st.columns([2, 1])
with c_col1:
    n1 = st.text_input("Nome Convidado 1", key="nome1", placeholder="Digite o nome...")
    n2 = st.text_input("Nome Convidado 2", key="nome2", placeholder="Digite o nome...")
with c_col2:
    t1 = st.selectbox("Cota 1", ["Ninguém", "Individual", "Casal"], key="tipo1")
    t2 = st.selectbox("Cota 2", ["Ninguém", "Individual", "Casal"], key="tipo2")

# --- LÓGICA DE COTAS ---
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

# 5. LANÇAMENTO DE VALORES
st.markdown("---")
with st.expander("📝 CLIQUE AQUI PARA LANÇAR OS VALORES (R$)", expanded=True):
    itens = ["Carne", "Pão de alho", "Linguiça", "Cerveja", "Jurupinga", "Vodka", "Fruta", "Carvão", "Gelo", "Outros"]
    col_v1, col_v2 = st.columns(2)
    v_gastos = {}

    for i, item in enumerate(itens):
        with col_v1 if i % 2 == 0 else col_v2:
            v_gastos[item] = st.number_input(f"{item}", min_value=0.0, step=5.0, format="%.2f")

total_geral = sum(v_gastos.values())

# --- CONTROLE DE ESTADO DO BOTÃO ---
if "calcular_clicado" not in st.session_state:
    st.session_state["calcular_clicado"] = False

# 6. BOTÃO CALCULAR
st.markdown("<br>", unsafe_allow_html=True)
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])

with col_btn2:
    if st.button("CALCULAR 🚀", use_container_width=True):
        if total_geral > 0:
            st.balloons() # Chuva de balões aqui!
            st.session_state["calcular_clicado"] = True
        else:
            st.warning("Preencha algum valor antes de calcular!")

# 7. EXIBIÇÃO DOS RESULTADOS (Só aparece se o botão foi clicado)
if st.session_state["calcular_clicado"] and total_geral > 0:
    st.divider()
    st.header(f"💰 Total Geral: R$ {total_geral:.2f}")
    
    if total_cotas > 0:
        valor_cota = total_geral / total_cotas
        
        # Resultados
        res1, res2 = st.columns(2)
        with res1:
            if v_guy: st.info(f"Família Guy: R$ {valor_cota*2:.2f}")
            if v_thi: st.info(f"Família Thi: R$ {valor_cota*2:.2f}")
            if val_c1 > 0: st.info(f"{n1}: R$ {valor_cota*val_c1:.2f}")
        with res2:
            if v_pau: st.info(f"Família Paulinho: R$ {valor_cota*2:.2f}")
            if v_jor: st.info(f"Jorge: R$ {valor_cota:.2f}")
            if val_c2 > 0: st.info(f"{n2}: R$ {valor_cota*val_c2:.2f}")

        # Montagem do Texto
        resumo = f"🍖 *CHURRASCO DO {anfitriao.upper()}* 🍖\n"
        resumo += f"📅 Data: {data_formatada}\n\n"
        resumo += f"💰 *Total: R$ {total_geral:.2f}*\n\n"
        
        if v_guy: resumo += f"👨‍👩‍👧‍👦 Família Guy: R$ {valor_cota*2:.2f}\n"
        if v_pau: resumo += f"👨‍👩‍👧‍👦 Família Paulinho: R$ {valor_cota*2:.2f}\n"
        if v_thi: resumo += f"👨‍👩‍👧‍👧 Família Thi: R$ {valor_cota*2:.2f}\n"
        if v_jor: resumo += f"❓ Jorge: R$ {valor_cota:.2f}\n"
        if val_c1 > 0: resumo += f"❓ {n1}: R$ {valor_cota*val_c1:.2f}\n"
        if val_c2 > 0: resumo += f"❓ {n2}: R$ {valor_cota*val_c2:.2f}\n"
        
        resumo += f"\n📍 *Pix para pagamento:* {chave_final}"

        st.subheader("📲 Enviar Resumo")
        st.text_area("Texto final:", resumo, height=250)
        
        link_zap = f"https://api.whatsapp.com/send?text={urllib.parse.quote(resumo)}"
        st.markdown(f"""
            <a href="{link_zap}" target="_blank" style="text-decoration: none;">
                <div style="width: 100%; background-color: #25D366; color: white; padding: 15px; text-
