import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Principal - FCARE", page_icon="📊", layout="wide")

st.title("📊 Dashboard Principal - FCARE")
st.write("Visão geral das transacções e estatísticas.")

# 🔹 Carregar dataset real
uploaded_file = st.file_uploader("Carregue um arquivo CSV com as transações", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    st.warning("Por favor, carregue um arquivo CSV para visualizar o dashboard.")
    st.stop()

# Criando coluna "Status"
df["Status"] = df["probabilidade_fraude"].apply(lambda x: "Suspeita" if x >= 0.75 else "Legítima")

# 🔹 Indicadores
col1, col2, col3 = st.columns(3)
col1.metric("Total de Transacções", len(df))
col2.metric("Fraudes Detectadas", (df["Status"] == "Suspeita").sum())
col3.metric("Taxa de Fraude (%)", round((df["Status"] == "Suspeita").mean() * 100, 2))

st.markdown("---")

# 🔹 Mostrar apenas transações com probabilidade de fraude >= 0.75
df_filtrado = df[df["probabilidade_fraude"] >= 0.75]

# 🔹 Tabela de transações
st.subheader("📄 Tabela de Transacções")
st.dataframe(df_filtrado, use_container_width=True)

# 🔹 Gráficos lado a lado
col_g1, col_g2 = st.columns(2)

with col_g1:
    st.subheader("📊 Distribuição (Barras)")
    status_counts = df["Status"].value_counts().reset_index()
    status_counts.columns = ["Status", "Quantidade"]
    fig_bar = px.bar(status_counts,
                     x="Status", y="Quantidade",
                     labels={"Status": "Status", "Quantidade": "Quantidade"},
                     color="Status")
    st.plotly_chart(fig_bar, use_container_width=True)

with col_g2:
    st.subheader("🥧 Distribuição (Pizza)")
    fig_pie = px.pie(df, names="Status", title="Proporção de Transações")
    st.plotly_chart(fig_pie, use_container_width=True)
