import streamlit as st
import urllib.parse
from datetime import datetime

# 1. Configuração inicial
st.set_page_config(page_title="Rachadinha Churrasco", page_icon="🍖")

# 2. Imagem de fundo e Playlist Spotify
fundo_url = "https://raw.githubusercontent.com/pmborba/Churrasco/main/WhatsApp%20Image%202026-01-08%20at%2014.55.05.jpeg"
spotify_playlist = "https://open.spotify.com/embed/playlist/37i9dQZF1DX10zKzsJ2jva?utm_source=generator" # Playlist Pagode

# 3. Banco de Dados Pix
chaves_pix = {
    "Guy": "064.266.399-82",
    "Thi": "064.514.089-99",
    "Paulinho": "085.994.129-90"
}

# 4. Estilo Visual (CSS)
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
    /* Estilo dos Inputs */
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
    /* Ajuste para o Expander (Lista de itens) */
    .streamlit-expanderHeader {{
        background-color: rgba(255, 255, 255, 0.4) !important;
        color: black !important;
        border-radius: 10px;
        font-weight: bold;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🍖 Rachadinha dos amigos 🍖")

# 5. Player de Música (Spotify)
st.markdown(f'<iframe style="border-radius:12px" src="{spotify_playlist}" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>', unsafe_allow_html=True)

# 6. Seleção de Anfitrião e Data
st.subheader("🏠 Dados do Evento")
col_local, col_data = st.columns(2)
with col_local:
    anfitriao = st.selectbox("Anfitrião:", ["Guy", "Thi", "Paulinho"])
    chave_final = chaves_pix.get(anfitriao)
with col_data:
    data_evento = st.date_input("Data:", datetime.now())

# 7. Participantes Fixos
st.subheader("👥 Quem participou?")
col_f1, col_f2 = st.columns(2)
with col_f1:
    v_guy = st.checkbox("Família Guy", value=True)
    v_thi = st.checkbox("Família Thi", value=True)
with col_f2:
    v_pau = st.checkbox("Família Paulinho", value=True)
    v_jor = st.checkbox("Jorge", value=True)

# 8. Convidados Extras
st.markdown("---")
st.write("👤 **Convidados Extras**")
c_col1, c_col2 = st.columns([2, 1])
with c_col1:
    n1 = st.text_input("Nome Convidado 1", key="nome1")
    n2 = st.text_input("Nome Convidado 2", key="nome2")
with c_col2:
    t1 = st.selectbox("Cota 1", ["Ninguém", "Individual", "Casal"], key="tipo1")
    t2 = st.selectbox("Cota 2", ["Ninguém", "Individual", "Casal"], key="tipo2")

# Lógica de Cotas
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

# 9. Lançamento de Valores (COM EXPANDER)
st.subheader("📝 Lançar Valores")

# Aqui está a mágica: O expander esconde a lista grande
with st.expander("Clique aqui para abrir a lista de itens 👇"):
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
    st.balloons() # Balões na tela! 🎈
    
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

        # Texto para WhatsApp
        data_fmt = data_evento.strftime("%d/%m/%Y")
        resumo = f"🍖 *CHURRASCO DO {anfitriao.upper()}* 🍖\n📅 Data: {data_fmt}\n\n"
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
                <div style="width: 100%; background-color: #25D366; color: white; padding: 15px; text-align: center; border-radius: 10px; font-weight: bold; font-size: 18px; box-shadow: 2px 2px 5px rgba(0,0,0,0.3);">
                    🚀 ENVIAR PARA WHATSAPP
                </div>
            </a>""", unsafe_allow_html=True)
    else:
        st.error("Selecione os participantes!")
else:
    st.info("👆 Abra a lista acima e lance os valores para calcular!")
