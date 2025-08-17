import streamlit as st

def mostrar_card(titulo, valor, cor="#007acc"):
    st.markdown(f"""
    <div style='background-color:{cor}; padding:20px; border-radius:10px; color:white; text-align:center;'>
        <h3>{titulo}</h3>
        <p style='font-size:24px;'>{valor}</p>
    </div>
    """, unsafe_allow_html=True)
