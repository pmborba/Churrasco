import streamlit as st

# Configuração da página
st.set_page_config(page_title="Churrasco 2026", page_icon="🍖")

st.title("🍖 Rachadinha dos amigos")
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
