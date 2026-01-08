import streamlit as st

# Link da sua foto no GitHub
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

    /* Textos do App (Títulos e Labels) */
    h1, h2, h3, p, label, .stMetric {{
        color: white !important;
        text-shadow: 2px 2px 4px #000000;
    }}

    /* CAMPOS DE ENTRADA E ÁREA DE TEXTO (Resumo) */
    /* Transparência 0.3 e Texto PRETO para legibilidade */
    .stNumberInput div div, .stNumberInput button, .stTextArea textarea {{
        background-color: rgba(255, 255, 255, 0.3) !important;
        color: black !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: bold !important;
    }}
    
    /* Garante que o texto digitado e o resumo fiquem pretos */
    input, textarea {{
        color: black !important;
        -webkit-text-fill-color: black !important;
    }}

    /* Ajuste para os alertas (Cotas) */
    .stAlert {{
        background-color: rgba(255, 255, 255, 0.15) !important;
        color: white !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🍖 Rachadinha dos amigos 🍖")

# ... (Mantenha sua lista de itens e o loop de gastos aqui) ...

# --- PARTE FINAL: RESULTADOS E WHATSAPP ---

if total_geral > 0:
    st.header(f"Total: R$ {total_geral:.2f}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.warning(f"**Casal (Família):**\n\nR$ {cota * 2:.2f}")
    with col2:
        st.success(f"**Jorge:**\n\nR$ {cota:.2f}")

    # Texto formatado
    resumo_zap = f"🍖 *RESUMO DO CHURRASCO* 🍖\n\n"
    resumo_zap += f"💰 Total Geral: R$ {total_geral:.2f}\n"
    resumo_zap += f"👨‍👩‍👧‍👦 Família (Casal): R$ {cota*2:.2f}\n"
    resumo_zap += f"👤 Jorge: R$ {cota:.2f}\n\n"
    resumo_zap += f"📍 Segue pix para pagamento:\n"
    resumo_zap += f"INSIRA_SEU_PIX_AQUI"

    st.subheader("📲 Resumo para Enviar")
    
    # Caixa de texto com o resumo (agora com fonte preta e fundo transparente)
    st.text_area(label="Texto pronto:", value=resumo_zap, height=220)
    
    # Botão de cópia nativo do Streamlit (funciona melhor que o ícone pequeno)
    st.copy_button(label="📋 Copiar Texto do Churrasco", text=resumo_zap)

else:
    st.write("Insira os valores para calcular.")
