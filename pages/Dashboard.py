import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Principal - FCARE", page_icon="📊", layout="wide")

st.title("📊 Dashboard Principal - FCARE")
st.write("Visão geral das transacções e estatísticas.")

if "dataset" in st.session_state:
    df = st.session_state["dataset"]
else:
    st.warning("Nenhum dataset carregado. Volte à página inicial e carregue o arquivo.")

# Criando coluna "status"
df["status"] = df["classe"].apply(lambda x: "Fraudulenta" if x == 1 else "Legítima")

# 🔹 Indicadores
col1, col2, col3 = st.columns(3)
col1.metric("Total de Transacções", len(df))
col2.metric("Fraudes Detectadas", (df["status"] == "Fraudulenta").sum())
col3.metric("Taxa de Fraude (%)", round((df["status"] == "Fraudulenta").mean()))

st.markdown("---")

# 🔹 Tabela de transações
st.subheader("📄 Tabela de Transacções")
st.dataframe(df)

# 🔹 Gráficos lado a lado
col_g1, col_g2 = st.columns(2)

with col_g1:
    st.subheader("📊 Distribuição (Barras)")
    status_counts = df["status"].value_counts().reset_index()
    status_counts.columns = ["status", "Quantidade"]
    fig_bar = px.bar(status_counts,
                     x="status", y="Quantidade",
                     labels={"status": "Status", "Quantidade": "Quantidade"},
                     color="status")
    st.plotly_chart(fig_bar, use_container_width=True)

with col_g2:
    st.subheader("🥧 Distribuição (Pizza)")
    fig_pie = px.pie(df, names="status", title="Proporção de Transações")
    st.plotly_chart(fig_pie, use_container_width=True)
