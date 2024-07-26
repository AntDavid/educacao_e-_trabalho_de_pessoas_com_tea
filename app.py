import streamlit as st



# Título
st.write(" # Educação e Trabalho de Pessoas com TEA")


# Conteúdos da barra lateral
st.sidebar.title("Navegação")
page = st.sidebar.radio("Ir para", ["Equipe", "Introdução", "Situação Escolar", "Nível de Escolarização", "Situação Laboral", "Trabalho por Cotas", "Municípios com Instituições", "Dados", "Conclusão"])

# Páginas
if (page == "Equipe"):
    from views.equipe import equipe
    equipe()


elif (page == "Introdução"):
    from views.introducao import introducao
    introducao()


elif (page == "Situação Escolar"):
    from views.situacao_escolar import situacao_escolar
    situacao_escolar()


elif (page == "Nível de Escolarização"):
    from views.nivel_escolarizacao import nivel_escolarizacao
    nivel_escolarizacao()


elif (page == "Situação Laboral"):
    from views.situacao_escolar import situacao_escolar
    situacao_escolar()    


elif (page == "Trabalho por Cotas"):
    from views.trabalho_cotas import trabalho_cotas
    trabalho_cotas()


elif (page == "Municípios com Instituições"):
    from views.trabalho_cotas import trabalho_cotas
    trabalho_cotas()


elif (page == "Dados"):
    from views.dados import dados
    dados()


elif (page == "Conclusão"):
    from views.conclusao import conclusao
    conclusao()

   