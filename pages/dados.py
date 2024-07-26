import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def dados(situacao_escolar, nivel_escolarizacao, idade_trabalho, trabalho_cotas, municipios_instituicoes):

    st.markdown("## Dados")
    st.markdown("### Situação Escolar por Faixa Etária")
    st.dataframe(situacao_escolar)

    st.markdown("### Nível de Escolarização")
    st.dataframe(nivel_escolarizacao)

    st.markdown("### Situação Laboral")
    st.dataframe(idade_trabalho)

    st.markdown("### Trabalho por Cotas")
    st.dataframe(trabalho_cotas)

    st.markdown("### Municípios com Instituições Cadastradas")
    st.dataframe(municipios_instituicoes)