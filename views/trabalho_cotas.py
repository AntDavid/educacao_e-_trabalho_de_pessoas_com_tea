import streamlit as st 
from modules.chart_generator import plot_bar_chart
import modules.read_database as rdb
 
def trabalho_cotas():
    st.markdown("## Trabalho por Cotas")
    st.markdown("""
        <div style='text-align: justify;'>
            A Lei de Cotas (Lei nº 8.213/1991) foi estabelecida para promover a inclusão no mercado de trabalho. Segundo os dados coletados pelo Ciptea, observa-se que a maioria das pessoas com TEA (83,08%) não está empregada. Focando apenas nas 101 pessoas que estão empregadas, descobrimos que 76,24% estão trabalhando fora da política de cotas, enquanto 23,76% se beneficiam dessa política. Esses dados destacam que uma grande parte da população com TEA, com 16 anos ou mais, permanece fora do mercado de trabalho, apesar do potencial de inclusão. Esse panorama ressalta a necessidade de desenvolver políticas públicas que facilitem o acesso e a inclusão no ambiente de trabalho, fundamental para garantir a autonomia, independência e cidadania dessa população.
            Além disso, é fundamental criar programas de capacitação e conscientização para empregadores, a fim de quebrar preconceitos e promover um ambiente de trabalho verdadeiramente inclusivo. Investir em suporte contínuo e adaptado às necessidades individuais pode aumentar significativamente as chances de sucesso e permanência dessas pessoas no mercado de trabalho. Garantir esses direitos não só promove a autonomia e independência das pessoas com TEA, mas também enriquece o ambiente de trabalho com diversidade e diferentes perspectivas, contribuindo para uma sociedade mais inclusiva e justa.
        </div>
    """, unsafe_allow_html=True)
    data = rdb.read_database()
    plot_bar_chart(data["trabalho cotas"], 'Trabalho', 'Total', 'Trabalho por Cotas', 'Trabalho', 'Número de Pessoas')
    st.markdown("""
        #### Fontes:
        https://www.faders.rs.gov.br/pesquisa-ciptea - Acesso em 19/07/2022\n
    """)