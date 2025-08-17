import streamlit as st
import pandas as pd

st.set_page_config(page_title="Transações Suspeitas - FCARE", page_icon="🚨", layout="wide")

st.title("🚨 Transações Suspeitas")
st.write("Lista de transações com probabilidade de fraude igual ou superior a **75%**.")

# 🔹 Carregar dataset real
uploaded_file = st.file_uploader("Carregue um arquivo CSV com as transações", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    st.warning("Por favor, carregue um arquivo CSV para visualizar o dashboard.")
    st.stop()

# Filtrando apenas suspeitas (≥75%)
df_suspeitas = df[df["probabilidade_fraude"] >= 0.75]

# Mostra tabela
st.dataframe(df_suspeitas, use_container_width=True)

# Selecionar transação para análise
st.subheader("🔍 Analisar Transação")
id_selecionado = st.selectbox("Selecione o ID da transação:", df_suspeitas["id"])

if id_selecionado:
    transacao = df_suspeitas[df_suspeitas["id"] == id_selecionado].iloc[0]
    st.write("**Usuário:**", transacao["nome"])
    st.write("**Valor:**", transacao["valor_gasto"])
    st.write("**Hora:**", transacao["tempo"])
    st.write("**Probabilidade:**", f"{transacao['probabilidade_fraude']*100:.1f}%")

    # Botão para histórico do usuário
    if st.button("📜 Ver Histórico do Usuário"):
        historico = df[df["nome"] == transacao["nome"]]
        st.write(f"Últimas transações do usuário **{transacao['nome']}**:")
        st.dataframe(historico)

    # Botões para confirmar ou rejeitar
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Confirmar Fraude"):
            st.success("Transação confirmada como fraude!")
    with col2:
        if st.button("❌ Rejeitar Suspeita"):
            st.info("Suspeita rejeitada. Transação marcada como legítima.")
