# import streamlit as st

# st.title("Teste de Conexão com Streamlit Cloud 🚀")

# st.write("Se você está vendo essa tela na nuvem, o deploy deu certo!")

# nome = st.text_input("Digite seu nome:")
# if nome:
#     st.success(f"Olá, {nome}! Tudo funcionando perfeitamente.")

import streamlit as st

# Título e subtítulo
st.title("🌐 Teste de Conexão com Streamlit Cloud")
st.subheader("Exemplos de componentes de texto")

# Texto simples
st.text("Este é um texto simples (sem formatação).")

# Markdown com formatação
st.markdown("""
## 🔧 Formatação com Markdown
Você pode usar **negrito**, *itálico*, `código inline`, listas:
- Item 1
- Item 2
- Item 3

E também [links clicáveis](https://streamlit.io)
""")

# Cabeçalhos e seções
st.header("📌 Sessão 1: Entrada de texto")

# Selectbox para tipo de texto
tipo_texto = st.selectbox("Selecione o tipo de texto:", ["Descrição", "Comentário", "Observação"])

# Input de texto
texto_entrada = st.text_area(f"Digite o texto do tipo '{tipo_texto}':")

if texto_entrada:
    st.info(f"Você digitou um texto do tipo **{tipo_texto}**:")
    st.write(texto_entrada)

nome = st.text_input("Digite seu nome:")
if nome:
    st.success(f"✅ Olá, {nome}! Tudo funcionando perfeitamente.")

descricao = st.text_area("Descreva o que você quer fazer com esse app:")
if descricao:
    st.info("📄 Descrição recebida:")
    st.write(descricao)

# Caixa de senha
senha = st.text_input("Digite uma senha de acesso", type="password")
if senha:
    st.warning("⚠️ Senha recebida (não armazenada).")

# Texto formatado dinamicamente
st.header("📊 Exemplo de campos simulando extração de nota")

equipe = "Mecânica"
hh = 4
materiais = ["Parafuso M8", "Chave 13mm", "Graxas"]

st.markdown(f"""
**Equipe executante:** `{equipe}`  
**Horas-Homem (HH):** `{hh}`  
**Materiais estimados:**  
- {materiais[0]}
- {materiais[1]}
- {materiais[2]}
""")

# Exibindo código (exemplo técnico)
st.header("💻 Exibindo trecho de código")
st.code("""def calcular_hh(pessoas, horas):
    return pessoas * horas
""", language="python")

# Exibindo uma fórmula matemática com LaTeX
st.header("🧠 Fórmula com LaTeX")
st.latex(r"HH = \text{nº de pessoas} \times \text{nº de horas}")

# Status e mensagens
st.header("📢 Mensagens de status")
st.success("✅ Operação concluída com sucesso.")
st.warning("⚠️ Esta é uma mensagem de atenção.")
st.error("❌ Ocorreu um erro ao salvar os dados.")
st.info("ℹ️ Este é um texto apenas informativo.")

# Fim
st.markdown("---")
st.caption("© 2025 - Exemplo criado por Diego com Streamlit 🚀")
