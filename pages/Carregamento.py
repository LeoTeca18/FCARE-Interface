import streamlit as st
import pandas as pd

st.set_page_config(page_title="Upload de Dataset", page_icon="📂", layout="centered")

st.title("📂 Upload do Dataset de Transações")

st.write("Por favor, carregue o arquivo **CSV**.")

# Colunas esperadas no CSV
colunas_esperadas = ["id", "nome", "valor_gasto", "categoria_compra", "hora", "tipo_transacao", "localizacao", "banco_emissor", "classe"]

# Upload do arquivo
arquivo = st.file_uploader("Selecione um arquivo CSV", type=["csv"])

df = None
csv_valido = False

if arquivo is not None:
    try:
        df = pd.read_csv(arquivo)
        st.write("Prévia dos dados carregados:")
        st.dataframe(df.head())

        # Verificação das colunas
        colunas_faltando = [col for col in colunas_esperadas if col not in df.columns]

        if colunas_faltando:
            st.error(f"❌ O arquivo está faltando as colunas obrigatórias: {', '.join(colunas_faltando)}")
        else:
            st.success("✅ Arquivo válido. Todas as colunas obrigatórias foram encontradas.")
            csv_valido = True
            st.session_state["dataset"] = df

    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")

# Chamar a função ou funções de processamento
