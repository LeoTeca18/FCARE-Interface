import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="FCARE - Detecção de Fraudes",
    page_icon="💳",
    layout="centered",
    initial_sidebar_state="collapsed"  # Oculta a barra lateral
)

# Fundo branco
st.markdown(
    """
    <style>
    body {
        background-color: white;
    }
    [data-testid="stSidebar"] {
        display: none;  /* Remove a barra lateral */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Cabeçalho
st.markdown("<h4 style='text-align: left;'>Deteção de Fraudes</h4>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: left; font-weight: bold;'>FCARE</h1>", unsafe_allow_html=True)

# Imagem centralizada
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("assets/FCACRE.png", width=300)

# Descrição
st.markdown(
    "<p style='text-align: center; font-size: 16px;'>Uma solução baseada em IA para a deteção de fraudes de cartões de crédito</p>",
    unsafe_allow_html=True
)

# Botão centralizado
col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    if st.button("Acessar"):
         st.switch_page("pages/Carregamento.py") # Link para a página do dashboard

# Estilo do botão com sombra
st.markdown(
    """
    <style>
    div.stButton > button {
        background-color: #00AEEF;
        color: white;
        padding: 12px 24px;
        font-size: 18px;
        border-radius: 10px;
        border: none;
        cursor: pointer;
        box-shadow: 2px 4px 10px rgba(0,0,0,0.2);
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #008CBA;
        box-shadow: 4px 6px 14px rgba(0,0,0,0.3);
        transform: scale(1.02);
    }
    </style>
    """,
    unsafe_allow_html=True
)
