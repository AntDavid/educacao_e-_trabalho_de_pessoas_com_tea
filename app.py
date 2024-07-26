import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Função para carregar dados
def load_data(file_path):
    return pd.read_csv(file_path)

# Carregar dados
situacao_escolar = load_data('./data/situacao_escolar.csv')
nivel_escolarizacao = load_data('./data/nivel_escolarizacao.csv')
idade_trabalho = load_data('./data/idade_trabalho.csv')
trabalho_cotas = load_data('./data/trabalho_cotas.csv')
municipios_instituicoes = load_data('./data/municipios_instituicoes.csv')

# Função para plotar gráfico de barras
def plot_bar_chart(data, x_col, y_col, title, xlabel, ylabel, rotate_xticks=False):
    plt.figure(figsize=(10, 6))
    plt.bar(data[x_col], data[y_col], color='red')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
   

    if rotate_xticks:
        plt.xticks(rotation=45, ha='right', fontsize= 10)
        plt.subplots_adjust(bottom=0.3)

    st.pyplot(plt)


def plot_pie_chart(labels, sizes, title):
    plt.figure(figsize=(4, 4))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=60, colors=['#66b3ff','#ff9999'])
    plt.title(title)
    st.pyplot(plt)


# Título
st.write(" # Educação e Trabalho de Pessoas com TEA")

# Conteúdos da barra lateral
st.sidebar.title("Navegação")
page = st.sidebar.radio("Ir para", ["Introdução", "Situação Escolar", "Nível de Escolarização", "Situação Laboral", "Trabalho por Cotas", "Municípios com Instituições", "Dados", "Conclusão"])

# Páginas
if page == "Equipe":
    st.markdown("""## Equipe""")
    st.markdown("""### Integrantes""")
    st.markdown("""- Ana Beatriz Salvino""")
    st.markdown("""- Antonio David Santa""")
    st.markdown("""- Erick Gabriel Araujo""")
    st.markdown("""- Telma Reis""")

elif page == "Introdução":
    st.markdown("""
    ## Introdução
    """)
    st.markdown("""
        <div style='text-align: justify;'>
            O Transtorno do Espectro Autista (TEA) é uma condição neurobiológica que impacta a percepção e a interação com o ambiente. No Brasil, a Lei Brasileira de Inclusão (Lei nº 13.146/2015) garante direitos fundamentais como educação e trabalho para pessoas com TEA. No entanto, a aplicação dessas leis ainda enfrenta desafios significativos.
        </div>
        <div style='text-align: justify;'>
            Este estudo analisa a situação atual da educação e do mercado de trabalho para pessoas com TEA, investigando dados sobre frequência escolar, nível de escolarização e participação no mercado de trabalho. A análise busca identificar as lacunas nas políticas de inclusão e destacar a necessidade de aprimorar o suporte para garantir uma verdadeira integração social e profissional.
        </div>
    """, unsafe_allow_html=True)
   


elif page == "Situação Escolar":
    st.markdown("## Situação Escolar por Faixa Etária")
    st.markdown("""
        <div style='text-align: justify;'>
            A Lei Brasileira de Inclusão da Pessoa com Deficiência (Lei nº 13.146/2015), em seu Artigo 27, estabelece que a educação é um direito fundamental para as pessoas com deficiência. A lei garante um sistema educacional inclusivo em todos os níveis, promovendo aprendizado contínuo ao longo da vida. O objetivo é alcançar o máximo desenvolvimento possível das habilidades físicas, sensoriais, intelectuais e sociais dos indivíduos, de acordo com suas características, interesses e necessidades de aprendizagem.
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: justify;'>
            Uma pesquisa sobre a frequência escolar das pessoas com Transtorno do Espectro Autista (TEA) revelou os seguintes resultados: entre as crianças de 0 a 5 anos (totalizando 1.455), que estão na faixa etária da educação infantil, 69,48% frequentam a escola. Na faixa de 6 a 15 anos (2.021 pessoas), correspondente ao ensino fundamental, 96,34% estão matriculados. Entre os jovens de 16 a 18 anos (196 indivíduos), faixa etária do ensino médio, 90,31% frequentam a escola. Entre 19 e 25 anos (186 pessoas), 47,85% ainda estão na escola. Para aqueles com mais de 26 anos (216 indivíduos), apenas 26,39% frequentam alguma instituição educacional. No grupo etário de 6 a 18 anos, 4,19% das pessoas com TEA não estão frequentando a escola.        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: justify;'>
            Para complementar, é importante salientar que a inclusão educacional das pessoas com TEA deve ser acompanhada de medidas adicionais, como a formação contínua de professores para lidar com as necessidades específicas desses alunos e a adaptação do ambiente escolar. O Atendimento Educacional Especializado (AEE) desempenha um papel crucial nesse contexto, fornecendo apoio individualizado que pode ajudar a aumentar a frequência e a permanência escolar. A implementação de políticas públicas eficazes é essencial para garantir que todas as crianças e jovens com TEA tenham acesso à educação de qualidade e possam desenvolver todo o seu potencial.
        </div>
    """, unsafe_allow_html=True)        
    plot_bar_chart(situacao_escolar, 'Faixa_Etaria', 'Frequenta_Escola', 'Situação Escolar por Faixa Etária - Frequenta Escola', 'Faixa_Etaria', 'Número de Pessoas')
    plot_bar_chart(situacao_escolar, 'Faixa_Etaria', 'Nao_Frequenta_Escola', 'Situação Escolar por Faixa Etária - Não Frequenta Escola', 'Faixa Etária', 'Número de Pessoas')
    st.markdown("""
        #### Fontes:
        https://www.faders.rs.gov.br/pesquisa-ciptea - Acesso em 19/07/2022\n
    """)

elif page == "Nível de Escolarização":
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
   
    
    plot_bar_chart(nivel_escolarizacao, 'Nivel_Escolar', 'Total', 'Nível de Escolarização', 'Nível Escolar', 'Número de Pessoas', rotate_xticks=True)
    st.markdown("""
        #### Fontes:
        https://www.faders.rs.gov.br/pesquisa-ciptea - Acesso em 19/07/2022\n
    """)
   

elif page == "Situação Laboral":
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
    plot_bar_chart(idade_trabalho, 'Idade', 'Total', 'Situação Laboral por Idade', 'Idade', 'Número de Pessoas')
    plt.subplots_adjust(bottom=0.3)
    st.markdown("""
        #### Fontes:
        https://www.faders.rs.gov.br/pesquisa-ciptea - Acesso em 19/07/2022\n
    """)

elif page == "Trabalho por Cotas":
    st.markdown("## Trabalho por Cotas")
    st.markdown("""
        <div style='text-align: justify;'>
            A Lei de Cotas (Lei nº 8.213/1991) foi estabelecida para promover a inclusão no mercado de trabalho. Segundo os dados coletados pelo Ciptea, observa-se que a maioria das pessoas com TEA (83,08%) não está empregada. Focando apenas nas 101 pessoas que estão empregadas, descobrimos que 76,24% estão trabalhando fora da política de cotas, enquanto 23,76% se beneficiam dessa política. Esses dados destacam que uma grande parte da população com TEA, com 16 anos ou mais, permanece fora do mercado de trabalho, apesar do potencial de inclusão. Esse panorama ressalta a necessidade de desenvolver políticas públicas que facilitem o acesso e a inclusão no ambiente de trabalho, fundamental para garantir a autonomia, independência e cidadania dessa população.
            Além disso, é fundamental criar programas de capacitação e conscientização para empregadores, a fim de quebrar preconceitos e promover um ambiente de trabalho verdadeiramente inclusivo. Investir em suporte contínuo e adaptado às necessidades individuais pode aumentar significativamente as chances de sucesso e permanência dessas pessoas no mercado de trabalho. Garantir esses direitos não só promove a autonomia e independência das pessoas com TEA, mas também enriquece o ambiente de trabalho com diversidade e diferentes perspectivas, contribuindo para uma sociedade mais inclusiva e justa.
        </div>
    """, unsafe_allow_html=True)
    plot_bar_chart(trabalho_cotas, 'Trabalho', 'Total', 'Trabalho por Cotas', 'Trabalho', 'Número de Pessoas')
    st.markdown("""
        #### Fontes:
        https://www.faders.rs.gov.br/pesquisa-ciptea - Acesso em 19/07/2022\n
    """)

elif page == "Municípios com Instituições":
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
    plt.bar(categories, values, color='skyblue')
    plt.xlabel('Categorias')
    plt.ylabel('Crescimento (%)')
    plt.title('Crescimento do Número de Escolas e Alunos no AEE no Ceará (2010-2017)')
    plt.figtext(0.99, 0.01, 'Fonte: scielo.br', horizontalalignment='right', fontsize=10, color='gray')
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

elif page == "Dados":
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

elif page == "Conclusão":
    st.markdown("""## Conclusão""")
    st.markdown("""
        <div style='text-align: justify;'>
            A análise dos dados sobre a situação escolar e laboral de pessoas com Transtorno do Espectro Autista (TEA) no Rio Grande do Sul revela uma realidade complexa e desafiadora. Embora existam avanços na inclusão educacional e laboral dessas pessoas, ainda há muitos obstáculos a serem superados para garantir seus direitos fundamentais e promover sua autonomia e independência.
        <div>
        <div style='text-align: justify;'>
            A baixa frequência escolar em algumas faixas etárias e a defasagem idade-série evidenciam a necessidade de políticas educacionais mais inclusivas e adaptadas às necessidades específicas das pessoas com TEA. O Atendimento Educacional Especializado (AEE) desempenha um papel crucial nesse contexto, fornecendo suporte individualizado que pode ajudar a aumentar a frequência e a permanência escolar desses alunos.
        <div>
        <div style='text-align: justify;'>                
            No âmbito laboral, a maioria das pessoas com TEA não está empregada, apesar do potencial de inclusão no mercado de trabalho. A implementação de políticas públicas e iniciativas que promovam a inclusão dessas pessoas é fundamental para garantir seu direito ao trabalho e sua participação na sociedade.
        </div>
    """, unsafe_allow_html=True)