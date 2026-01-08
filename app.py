import streamlit as st
import urllib.parse

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
    .stNumberInput div div, .stNumberInput button, .stTextArea textarea {{
        background-color: rgba(255, 255, 255, 0.3) !important;
        border: none !important;
        border-radius: 10px !important;
    }}
    input, textarea {{
        color: black !important;
        -webkit-text-fill-color: black !important;
        font-weight: bold !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🍖 Rachadinha dos amigos 🍖")

# --- LISTA DE ITENS ---
itens = ["Carne", "Pão de alho", "Linguiça", "Cerveja", "Jurupinga", "Vodka", "Fruta", "Carvão", "Gelo", "Outros valores"]
gastos = {}

st.subheader("📝 Lançar Valores")
for item in itens:
    gastos[item] = st.number_input(f"{item} (R$)", min_value=0.0, value=0.0, step=5.0, format="%.2f")

# --- CÁLCULOS ---
total_geral = sum(gastos.values())
cota = total_geral / 7

if total_geral > 0:
    st.divider()
    st.header(f"Total: R$ {total_geral:.2f}")
    
    c1, c2 = st.columns(2)
    c1.metric("Casal (Família)", f"R$ {cota * 2:.2f}")
    c2.metric("Jorge", f"R$ {cota:.2f}")

    # --- FORMATANDO TEXTO ---
    resumo_zap = f"🍖 *RESUMO DO CHURRASCO* 🍖\n\n"
    resumo_zap += f"💰 Total: R$ {total_geral:.2f}\n"
    resumo_zap += f"👨‍👩‍👧‍👦 Família: R$ {cota*2:.2f}\n"
    resumo_zap += f"👤 Jorge: R$ {cota:.2f}\n\n"
    resumo_zap += f"📍 Pix: SUA_CHAVE_AQUI"

    # Criando o link do WhatsApp
    texto_url = urllib.parse.quote(resumo_zap)
    link_whatsapp = f"https://wa.me/?text={texto_url}"

    st.subheader("📲 Enviar para o Grupo")
    
    # Exibe o texto para conferência
    st.text_area("Texto que será enviado:", value=resumo_zap, height=180)
    
    # BOTÃO QUE ABRE O WHATSAPP DIRETO
    st.markdown(
        f"""
        <a href="{link_whatsapp}" target="_blank">
            <button style="
                width: 100%;
                background-color: #25D366;
                color: white;
                padding: 15px;
                border: none;
                border-radius: 10px;
                font-weight: bold;
                font-size: 18px;
                cursor: pointer;
                box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
            ">
                🚀 ENVIAR PARA O WHATSAPP
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )
else:
    st.write("Insira os valores para calcular.")
