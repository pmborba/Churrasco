import streamlit as st

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

    /* Textos do App (Títulos e Labels) */
    h1, h2, h3, p, label, .stMetric {{
        color: white !important;
        text-shadow: 2px 2px 4px #000000;
    }}

    /* CAMPOS DE ENTRADA E ÁREA DE TEXTO (Resumo) */
    .stNumberInput div div, .stNumberInput button, .stTextArea textarea {{
        background-color: rgba(255, 255, 255, 0.3) !important;
        border: none !important;
        border-radius: 10px !important;
    }}
    
    /* COR DA FONTE: PRETA nos campos e no resumo */
    input, textarea {{
        color: black !important;
        -webkit-text-fill-color: black !important;
        font-weight: bold !important;
    }}

    /* Alertas de resultado */
    .stAlert {{
        background-color: rgba(255, 255, 255, 0.15) !important;
        color: white !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🍖 Rachadinha dos amigos 🍖")
st.info("Divisão: 3 Famílias (2 cotas cada) + Jorge (1 cota) = 7 cotas")

# --- LISTA DE ITENS ATUALIZADA (Com "Outros valores") ---
itens = [
    "Carne", "Pão de alho", "Linguiça", "Cerveja", 
    "Jurupinga", "Vodka", "Fruta", "Carvão", "Gelo", "Outros valores"
]

gastos = {}

st.subheader("📝 Lançar Valores")
for item in itens:
    gastos[item] = st.number_input(f"{item} (R$)", min_value=0.0, value=0.0, step=5.0, format="%.2f")

# --- CÁLCULOS ---
total_geral = sum(gastos.values())
cota = total_geral / 7

st.divider()

# --- RESULTADOS E WHATSAPP ---
if total_geral > 0:
    st.header(f"Total: R$ {total_geral:.2f}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.warning(f"**Casal (Família):**\n\nR$ {cota * 2:.2f}")
    with col2:
        st.success(f"**Jorge:**\n\nR$ {cota:.2f}")

    # Montagem do texto para o Zap
    resumo_zap = f"🍖 *RESUMO DO CHURRASCO* 🍖\n\n"
    resumo_zap += f"💰 Total Geral: R$ {total_geral:.2f}\n"
    resumo_zap += f"👨‍👩‍👧‍👦 Família (Casal): R$ {cota*2:.2f}\n"
    resumo_zap += f"👤 Jorge: R$ {cota:.2f}\n\n"
    resumo_zap += f"📍 Segue pix para pagamento:\n"
    resumo_zap += "SUA_CHAVE_PIX_AQUI" 

    st.subheader("📲 Resumo para Enviar")
    st.text_area(label="Texto pronto para o grupo:", value=resumo_zap, height=220)
    st.copy_button(label="📋 Copiar Texto do Churrasco", text=resumo_zap)

else:
    st.write("Insira os valores acima para calcular a divisão.")
