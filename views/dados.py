import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import modules.read_database as rdb


def dados():
    data = rdb.read_database()
    st.markdown("## Dados")
    st.markdown("### Situação Escolar por Faixa Etária")
    st.dataframe(data["situacao escolar"])


    st.markdown("### Nível de Escolarização")
    st.dataframe(data["nivel escolarizacao"])

    st.markdown("### Situação Laboral")
    st.dataframe(data["idade trabalho"])

    st.markdown("### Trabalho por Cotas")
    st.dataframe(data["trabalho cotas"])

    st.markdown("### Municípios com Instituições Cadastradas")
    st.dataframe(data["municipios instituicoes"])