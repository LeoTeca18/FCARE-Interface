import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Histórico do Usuário", page_icon="📜", layout="wide")

# Título
st.title("📜 Histórico do Usuário")

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

# Exibir tabela das transações do usuário selecionado
st.subheader(f"📊 Transações Passadas de {transacao['nome']}")
historico_usuario = df[df["nome"] == transacao["nome"]].sort_values("tempo", ascending=False)
st.dataframe(historico_usuario, use_container_width=True)

# Cálculo das métricas do usuário
media_gastos_usuario = historico_usuario["valor_gasto"].mean()
freq_transacoes_usuario = len(historico_usuario) / ((historico_usuario["tempo"].max() - historico_usuario["tempo"].min())) if len(historico_usuario) > 1 else len(historico_usuario)

col1, col2 = st.columns(2)
with col1:
    st.metric("💰 Média de Gastos (Usuário)", f"{media_gastos_usuario:.2f} Kz")
with col2:
    st.metric("📅 Frequência Média (Usuário)", f"{freq_transacoes_usuario:.1f} transações")

# Gráfico de tendência do usuário
st.subheader(f"📈 Tendência de Gastos de {transacao['nome']}")
df_grouped_usuario = historico_usuario.groupby("tempo")["valor_gasto"].sum()

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(df_grouped_usuario.index, df_grouped_usuario.values, marker='o')
ax.set_title(f"Tendência de Gastos de {transacao['nome']} ao Longo do Tempo")
ax.set_xlabel("Hora")
ax.set_ylabel("Valor Total (Kz)")
ax.grid(True)
st.pyplot(fig)