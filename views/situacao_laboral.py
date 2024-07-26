import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
from modules.chart_generator import plot_bar_chart
import modules.read_database as rdb

def situacao_laboral():
    st.markdown("## Situação Laboral")
    st.markdown("""
        <div style='text-align: justify;'>
            De acordo com a Lei nº 13.146/2015, conhecida como Lei Brasileira de Inclusão da Pessoa com Deficiência, o artigo 34 assegura que "a pessoa com deficiência tem direito ao trabalho de sua livre escolha e aceitação, em ambiente acessível e inclusivo, em igualdade de oportunidades com as demais pessoas". No entanto, embora muitas pessoas com TEA estejam em idade para trabalhar (acima de 16 anos), uma expressiva maioria (83,44%) não está empregada.
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: justify;'>
            Esse cenário sublinha a necessidade urgente de implementar e reforçar políticas públicas e iniciativas que promovam a inclusão dessas pessoas no mercado de trabalho. Além de criar ambientes de trabalho acessíveis e inclusivos, é crucial oferecer suporte adequado para a formação e capacitação profissional, visando garantir que as pessoas com TEA tenham as mesmas oportunidades de emprego e desenvolvimento profissional que as demais. Somente com esforços contínuos e coordenados será possível promover a autonomia, independência e plena cidadania dessa população.
        </div>
    """, unsafe_allow_html=True)

    data = rdb.read_database()
    plot_bar_chart(data["idade trabalho"], 'Idade', 'Total', 'Situação Laboral por Idade', 'Idade', 'Número de Pessoas')
    plt.subplots_adjust(bottom=0.3)
    st.markdown("""
        #### Fontes:
        https://www.faders.rs.gov.br/pesquisa-ciptea - Acesso em 19/07/2022\n
    """)