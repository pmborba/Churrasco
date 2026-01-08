import streamlit as st

# Substitua o link abaixo pelo seu link do GitHub
fundo_url = "https://raw.githubusercontent.com/pmborba/Churrasco/main/WhatsApp%20Image%202026-01-08%20at%2014.55.05.jpeg"

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

    /* Textos brancos com sombra para leitura */
    h1, h2, h3, p, label, .stMetric, .stMarkdown {{
        color: white !important;
        text-shadow: 2px 2px 4px #000000;
    }}

    /* CAMPOS DE ENTRADA E ÁREA DE TEXTO (Resumo Zap) */
    .stNumberInput div div, .stNumberInput button, .stTextArea textarea {{
        background-color: rgba(255, 255, 255, 0.3) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
    }}
    
    /* Cor do texto dentro da área de texto */
    .stTextArea textarea {{
        color: white !important;
        font-weight: normal !important;
    }}

    /* Garante que o número digitado fique visível */
    input {{
        color: white !important;
        font-weight: bold !important;
        background-color: transparent !important;
    }}

    /* Alertas (Cotas) também transparentes */
    .stAlert {{
        background-color: rgba(255, 255, 255, 0.15) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🍖 Rachadinha dos amigos 🍖")
st.info("Divisão: 3 Famílias (2 cotas cada) + Jorge (1 cota) = 7 cotas")

itens = [
    "Carne", "Pão de alho", "Linguiça", "Cerveja", 
    "Jurupinga", "Vodka", "Fruta", "Carvão", "Gelo", "Outros"
]

gastos = {}

st.subheader("📝 Lançar Valores")
for item in itens:
    gastos[item] = st.number_input(f"{item} (R$)", min_value=0.0, value=0.0, step=5.0, format="%.2f")

total_geral = sum(gastos.values())
cota = total_geral / 7

st.divider()

if total_geral > 0:
    st.header(f"Total: R$ {total_geral:.2f}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.warning(f"**Casal (Cada Família):**\n\nR$ {cota * 2:.2f}")
    with col2:
        st.success(f"**Jorge (Individual):**\n\nR$ {cota:.2f}")

    # --- FORMATAÇÃO DO TEXTO PARA WHATSAPP ---
    resumo_zap = f"🍖 *RESUMO DO CHURRASCO* 🍖\n\n"
    resumo_zap += f"💰 Total Geral: R$ {total_geral:.2f}\n"
    resumo_zap += f"👨‍👩‍👧‍👦 Família (Casal): R$ {cota*2:.2f}\n"
    resumo_zap += f"👤 Jorge: R$ {cota:.2f}\n\n"
    resumo_zap += f"📍 Segue pix para pagamento:\n"
    resumo_zap += f"SUA_CHAVE_PIX_AQUI" # COLOQUE SUA CHAVE AQUI

    st.subheader("📲 Copiar para WhatsApp")
    # O componente abaixo já exibe um ícone de "copiar" no canto superior direito ao passar o mouse
    st.text_area(label="Clique no ícone no canto direito para copiar:", value=resumo_zap, height=200)
else:
    st.write("Insira os valores para calcular.")
