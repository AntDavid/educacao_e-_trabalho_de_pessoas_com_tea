import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt 
from modules.chart_generator import plot_bar_chart
import modules.read_database as rdb


def situacao_escolar():
    st.markdown("## Situação Escolar por Faixa Etária")
    st.markdown("""
        <div style='text-align: justify;'>
            A Lei Brasileira de Inclusão da Pessoa com Deficiência (Lei nº 13.146/2015), em seu Artigo 27, estabelece que a educação é um direito fundamental para as pessoas com deficiência. A lei garante um sistema educacional inclusivo em todos os níveis, promovendo aprendizado contínuo ao longo da vida. O objetivo é alcançar o máximo desenvolvimento possível das habilidades físicas, sensoriais, intelectuais e sociais dos indivíduos, de acordo com suas características, interesses e necessidades de aprendizagem.
        </div>
        """, unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: justify;'>
            Uma pesquisa sobre a frequência escolar das pessoas com Transtorno do Espectro Autista (TEA) revelou os seguintes resultados: entre as crianças de 0 a 5 anos (totalizando 1.455), que estão na faixa etária da educação infantil, 69,48% frequentam a escola. Na faixa de 6 a 15 anos (2.021 pessoas), correspondente ao ensino fundamental, 96,34% estão matriculados. Entre os jovens de 16 a 18 anos (196 indivíduos), faixa etária do ensino médio, 90,31% frequentam a escola. Entre 19 e 25 anos (186 pessoas), 47,85% ainda estão na escola. Para aqueles com mais de 26 anos (216 indivíduos), apenas 26,39% frequentam alguma instituição educacional. No grupo etário de 6 a 18 anos, 4,19% das pessoas com TEA não estão frequentando a escola.
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: justify;'>
            Para complementar, é importante salientar que a inclusão educacional das pessoas com TEA deve ser acompanhada de medidas adicionais, como a formação contínua de professores para lidar com as necessidades específicas desses alunos e a adaptação do ambiente escolar. O Atendimento Educacional Especializado (AEE) desempenha um papel crucial nesse contexto, fornecendo apoio individualizado que pode ajudar a aumentar a frequência e a permanência escolar. A implementação de políticas públicas eficazes é essencial para garantir que todas as crianças e jovens com TEA tenham acesso à educação de qualidade e possam desenvolver todo o seu potencial.
        </div>
    """, unsafe_allow_html=True)        
    
    data = rdb.read_database()
    plot_bar_chart(data["situacao escolar"], 'Faixa_Etaria', 'Frequenta_Escola', 'Situação Escolar por Faixa Etária - Frequenta Escola', 'Faixa_Etaria', 'Número de Pessoas')
    plot_bar_chart(data["situacao escolar"], 'Faixa_Etaria', 'Nao_Frequenta_Escola', 'Situação Escolar por Faixa Etária - Não Frequenta Escola', 'Faixa Etária', 'Número de Pessoas')
    st.markdown("""
        #### Fontes:
        https://www.faders.rs.gov.br/pesquisa-ciptea - Acesso em 19/07/2022\n
    """)