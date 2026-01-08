import streamlit as st

# Substitua o link abaixo pelo que você copiou no passo anterior
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
    }}
    /* Deixando os textos brancos para aparecerem sobre a foto */
    h1, h2, h3, p, label, .stMetric {{
        color: white !important;
    }}
    /* Fundo dos campos de entrada levemente escuro para leitura */
    .stNumberInput div {{
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 5px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🍖 Rachadinha dos amigos 🍖")
st.info("Divisão: 3 Famílias (2 cotas cada) + Jorge (1 cota) = 7 cotas")

# Lista de itens conforme solicitado
itens = [
    "Carne", "Pão de alho", "Linguiça", "Cerveja", 
    "Jurupinga", "Vodka", "Fruta", "Carvão", "Gelo"
]

gastos = {}

# Criando os campos de entrada
st.subheader("📝 Lançar Valores")
for item in itens:
    gastos[item] = st.number_input(f"{item} (R$)", min_value=0.0, value=0.0, step=5.0, format="%.2f")

# Cálculos
total_geral = sum(gastos.values())
cota = total_geral / 7

st.divider()

# Resultados
if total_geral > 0:
    st.header(f"Total: R$ {total_geral:.2f}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.warning(f"**Casal (Cada Família):**\n\nR$ {cota * 2:.2f}")
    with col2:
        st.success(f"**Jorge (Individual):**\n\nR$ {cota:.2f}")

    # Texto para WhatsApp
    resumo_zap = f"*Resumo do Churrasco*\n\n"
    resumo_zap += f"Total: R$ {total_geral:.2f}\n"
    resumo_zap += f"Cada Família: R$ {cota*2:.2f}\n"
    resumo_zap += f"Jorge: R$ {cota:.2f}"
    
    st.text_area("Copie para o WhatsApp:", resumo_zap)
else:
    st.write("Insira os valores para calcular.")
