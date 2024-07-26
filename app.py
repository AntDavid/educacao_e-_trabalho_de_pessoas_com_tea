import streamlit as st


# Função para plotar gráfico de barras



# Título
st.write(" # Educação e Trabalho de Pessoas com TEA")

# Conteúdos da barra lateral
st.sidebar.title("Navegação")
page = st.sidebar.radio("Ir para", ["Equipe", "Introdução", "Situação Escolar", "Nível de Escolarização", "Situação Laboral", "Trabalho por Cotas", "Municípios com Instituições", "Dados", "Conclusão"])

# Páginas
if (page == "Equipe"):
    from pages.equipe import equipe
    equipe()


elif (page == "Introdução"):
    from pages.introducao import introducao
    introducao()


elif (page == "Situação Escolar"):
    from pages.situacao_escolar import situacao_escolar
    situacao_escolar()


elif (page == "Nível de Escolarização"):
    from pages.nivel_escolarizacao import nivel_escolarizacao
    nivel_escolarizacao()


elif (page == "Situação Laboral"):
    from pages.situacao_escolar import situacao_escolar
    situacao_escolar()    


elif (page == "Trabalho por Cotas"):
    from pages.trabalho_cotas import trabalho_cotas
    trabalho_cotas()


elif (page == "Municípios com Instituições"):
    from pages.trabalho_cotas import trabalho_cotas
    trabalho_cotas()


elif (page == "Dados"):
    from pages.dados import dados
    dados()


elif (page == "Conclusão"):
    from pages.conclusao import conclusao
    conclusao()