import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from modules.chart_generator import plot_bar_chart
import modules.read_database as rdb


def nivel_escolarizacao():
    st.markdown("## Nível de Escolarização")
    st.markdown("""
        <div style='text-align: justify;'>
            Em relação ao nível de escolaridade, os dados indicam que 4,98% das pessoas relataram nunca ter frequentado uma escola, enquanto 33,87% frequentaram ou estão atualmente na educação infantil. Esse resultado é compreensível, considerando que 34,11% das pessoas assistidas pela Ciptea têm entre 0 e 5 anos de idade.\n
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: justify;'>
            Ao analisar as informações cruzadas entre idade e nível de escolaridade, verifica-se que existe uma discrepância significativa: 15,64% das crianças com TEA estão na faixa etária de 6 a 7 anos e deveriam estar no 1º ano do ensino fundamental, mas apenas 10,21% estão realmente matriculadas nesse nível. Isso evidencia uma defasagem idade-série.
            Além disso, os dados revelam que 3,61% da população com TEA possui graduação, 0,93% concluiu pós-graduação, 0,29% alcançou o nível de mestrado e 0,15% obteve doutorado. Esses números mostram que, embora existam pessoas com TEA que atingiram altos níveis de educação, a maioria ainda enfrenta barreiras significativas no acesso e na permanência escolar.                    
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: justify;'>
            Para complementar, é fundamental destacar a importância de políticas educacionais inclusivas que possam mitigar essas disparidades. Programas de suporte, como o Atendimento Educacional Especializado (AEE), são essenciais para garantir que crianças com TEA recebam a ajuda necessária desde cedo, prevenindo a defasagem idade-série e promovendo um ambiente de aprendizado mais equitativo. Além disso, a formação contínua de educadores e a adaptação dos currículos escolares são passos cruciais para atender adequadamente às necessidades desses alunos, incentivando sua progressão acadêmica e pessoal.
        </div>
    """, unsafe_allow_html=True)
    
    data = rdb.read_database()        
    plot_bar_chart(data["nivel escolarizacao"], 'Nivel_Escolar', 'Total', 'Nível de Escolarização', 'Nível Escolar', 'Número de Pessoas', rotate_xticks=True)
    st.markdown("""
        #### Fontes:
        https://www.faders.rs.gov.br/pesquisa-ciptea - Acesso em 19/07/2022\n
    """)