import streamlit as st

st.title("Teste de Conexão com Streamlit Cloud 🚀")

st.write("Se você está vendo essa tela na nuvem, o deploy deu certo!")

nome = st.text_input("Digite seu nome:")
if nome:
    st.success(f"Olá, {nome}! Tudo funcionando perfeitamente.")
