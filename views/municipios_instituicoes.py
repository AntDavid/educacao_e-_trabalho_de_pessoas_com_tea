import streamlit as st 
import matplotlib.pyplot as plt
from modules.chart_generator import plot_pie_chart

def municipios_instituicoes():
    st.markdown(" ### Municípios com Instituições Cadastradas no Rio Grande do Sul \n")
    st.markdown("""
        <div style='text-align: justify;'>
            Para facilitar o acesso ao processo de solicitação da Ciptea (Carteira de Identificação da Pessoa com Transtorno do Espectro Autista) para famílias com dificuldades, foram firmadas parcerias com instituições de apoio, como associações para pessoas com Transtorno do Espectro Autista, APAEs e CRAS. Essas instituições auxiliam no preenchimento e entrega do formulário de solicitação, tornando o processo mais democrático e inclusivo. Desde junho de 2021, foi iniciado um cadastramento de instituições para oferecer esse apoio, resultando em 257 instituições cadastradas em 211 municípios do Rio Grande do Sul, cobrindo 42,9% dos municípios.
        </div>\n
    """, unsafe_allow_html=True)
    plot_pie_chart(['Sim', 'Não'], [42.9, 100-42.9], 'Percentual de Municípios com Instituições Cadastradas no Rio Grande do Sul')

    st.markdown("\n ### Estimativas de escolas que oferecem atendimento educacional especializado no Brasil (2022)\n")
    st.markdown("""
        <div style='text-align: justify;'>
            De acordo com os dados mais recentes, apenas 21,5% das escolas de educação básica no Brasil oferecem Atendimento Educacional Especializado (AEE) através de salas de recursos multifuncionais (SRMs). Esse percentual corresponde a 38.314 das 178.346 escolas de educação básica no país. Este número revela uma cobertura limitada do AEE, indicando que uma proporção significativa de escolas ainda não conta com esses recursos especializados.
        </div>
        <div style='text-align: justify;'>
            Além disso, o Brasil enfrenta um déficit de profissionais para o AEE. Em 2022, havia apenas 51,3 mil professores especializados para atender a demanda de estudantes com necessidades educacionais especiais, o que sugere uma carência substancial na oferta desses serviços. Este déficit é uma preocupação importante, pois limita a capacidade das escolas em fornecer o suporte necessário para a inclusão e o desenvolvimento adequado desses alunos.
        </div>
        <div style='text-align: justify;'>
            Os modelos de AEE em uso incluem o atendimento no contraturno, que é o mais comum, onde o AEE ocorre em um horário diferente do período escolar, geralmente na própria escola ou em uma instituição regular próxima. Outro modelo é o itinerante, no qual um profissional do AEE atua em várias escolas, oferecendo orientação e apoio aos professores e à gestão escolar. O modelo híbrido combina atendimento presencial e remoto, especialmente relevante durante a pandemia, quando as escolas precisaram adaptar suas práticas para manter a continuidade do ensino. Por fim, o modelo colaborativo envolve o planejamento pedagógico conjunto entre o professor do AEE e o professor regente, promovendo uma abordagem mais integrada e inclusiva.
                A análise dos dados também revela a presença de modelos de AEE não regulamentados, como o AEE hospitalar e domiciliar, que carecem de políticas públicas e diretrizes específicas. A ausência de regulamentação para esses formatos destaca a necessidade de desenvolvimento de políticas que garantam uma cobertura mais ampla e inclusiva.
        </div>
        <div style='text-align: justify;'>
            A baixa cobertura das SRMs e o déficit de profissionais especializados indicam a necessidade urgente de investimentos para expandir a oferta do AEE e melhorar a formação e a quantidade de profissionais disponíveis. A integração eficaz dos diferentes modelos de AEE e a criação de políticas públicas que abordem todas as formas de atendimento especial são essenciais para promover uma educação mais inclusiva e acessível para todos os estudantes com necessidades especiais no Brasil.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("\n ### Crescimento do Número de Escolas e Alunos no AEE no Ceará (2010-2017)\n")
    st.markdown("""
        <div style='text-align: justify;'>
            No estado do Ceará, entre 2010 e 2017, o número de alunos matriculados no AEE cresceu 335,33%, enquanto o número de escolas com AEE não exclusivas aumentou 434,93% e as exclusivas cresceram 611,11%. Em Fortaleza, o número de escolas com AEE cresceu 195,65% no mesmo período. No entanto, apenas 50% dos alunos com    necessidades especiais no Ceará e 58% em Fortaleza tinham acessoao AEE em 2017, indicando uma necessidade de expansão desse atendimento
        </div>
    """, unsafe_allow_html=True)
    categories = ['Alunos no AEE', 'Escolas AEE Não Exclusivas', 'Escolas AEE Exclusivas', 'Escolas com AEE em Fortaleza']
    values = [335.33, 434.93, 611.11, 195.65]  

        
    plt.figure(figsize=(10, 6))
    plt.bar(categories, values, color='red')
    plt.xlabel('Categorias')
    plt.ylabel('Crescimento (%)')
    plt.title('Crescimento do Número de Escolas e Alunos no AEE no Ceará (2010-2017)')
    plt.figtext(0.99, 0.01, 'Fonte: scielo.br', horizontalalignment='right', fontsize=10, color='red')
    plt.xticks(rotation=45)
    st.pyplot(plt)

    st.markdown("""
        <div style='text-align: justify;'>
            Um estudo avaliou o impacto do AEE sobre a defasagem idade-série dos alunos com necessidades especiais, utilizando dados do Censo Escolar da Educação Básica de 2016. O estudo observou que, embora haja um aumento no número de alunos com necessidades especiais no ensino regular, o nível de aprendizagem ainda é baixo. Isso sugere a necessidade de políticas de suporte, como o AEE, para melhorar a aprendizagem e a permanência escolar desses alunos. Além disso, vale ressaltar a importância da formação de professores para atender às necessidades específicas dos alunos com deficiência, a fim de promover uma educação inclusiva e de qualidade.
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        #### Fontes:\n
        https://www.faders.rs.gov.br/pesquisa-ciptea - Acesso em 19/07/2022\n
        http://diversa.org.br/noticias/conheca-os-modelos-de-atendimento-educacional-especializado-aee/ - Acesso em 22/07/2022\n
        https://www.gov.br/inep/pt-br/assuntos/noticias/censo-escolar/mec-e-inep-divulgam-resultados-do-censo-escolar-2023 - Acesso em 22/07/2022\n
        https://www.scielo.br/j/ep/a/HmS58qB4qSGXLzsSRJzx43B/ - Acesso em 22/07/2022
    """)
