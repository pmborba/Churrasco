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
    h1, h2, h3, p, label, .stMetric {{
        color: white !important;
        text-shadow: 2px 2px 4px #000000;
    }}

    /* CAMPOS DE ENTRADA: 50% Transparentes */
    .stNumberInput div div {{
        background-color: rgba(255, 255, 255, 0.5) !important;
        color: black !important;
        border-radius: 10px;
    }}
    
    /* Ajuste da cor do texto dentro do campo para não sumir */
    input {{
        color: black !important;
        font-weight: bold;
    }}

    /* Deixar o fundo das áreas de texto e info também transparentes */
    .stAlert, .stTextArea textarea {{
        background-color: rgba(255, 255, 255, 0.2) !important;
        color: white !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🍖 Rachadinha dos amigos 🍖")
st.info("Divisão: 3 Famílias (2 cotas cada) + Jorge (1 cota) = 7 cotas")

# Lista de itens
itens = [
    "Carne", "Pão de alho", "Linguiça", "Cerveja", 
    "Jurupinga", "Vodka", "Fruta", "Carvão", "Gelo"
]

gastos = {}

# Criando os campos de entrada
st.subheader("📝 Lançar Valores")
for item in itens:
    # Usei o label do campo para os gastos
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
