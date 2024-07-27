import streamlit as st

st.set_page_config(page_title="Educação e Trabalho de Pessoas com TEA", page_icon="🧩", layout="wide")

st.sidebar.title("Navegação")

page = st.sidebar.radio("ir para",[
    "Equipe",
    "Introdução",
    "Situação Escolar",
    "Nível de Escolarização",
    "Situação Laboral",
    "Trabalho por Cotas",
    "Municípios com Instituições",
    "Dados",
    "Conclusão"
])

pages = {
    "Equipe": "views.equipe.equipe",
    "Introdução": "views.introducao.introducao",
    "Situação Escolar": "views.situacao_escolar.situacao_escolar",
    "Nível de Escolarização": "views.nivel_escolarizacao.nivel_escolarizacao",
    "Situação Laboral": "views.situacao_laboral.situacao_laboral",
    "Trabalho por Cotas": "views.trabalho_cotas.trabalho_cotas",
    "Municípios com Instituições": "views.municipios_instituicoes.municipios_instituicoes",
    "Dados": "views.dados.dados",
    "Conclusão": "views.conclusao.conclusao"
}


def load_page(page_name):
    module_path, function_name = pages[page_name].rsplit('.', 1)
    module = __import__(module_path, globals(), fromlist=[function_name])
    function = getattr(module, function_name)
    function()

load_page(page)
