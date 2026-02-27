# 📊 Educação e Trabalho de Pessoas com TEA

> Trabalho de pesquisa e análise de dados desenvolvido durante o curso PAIDEIA-LASSU da USP.

Este projeto tem como objetivo analisar e visualizar dados sobre a situação escolar e laboral de pessoas com Transtorno do Espectro Autista (TEA). Através da coleta, processamento e visualização de dados públicos, buscamos trazer insights relevantes sobre a inclusão educacional e o acesso ao mercado de trabalho para essa população.

---

## 🔍 Fontes de Dados e Pesquisa

A análise desenvolvida neste repositório foi fundamentada e complementada pelas seguintes bases de dados e pesquisas oficiais:

* **[Faders - Pesquisa CIPTEA](https://www.faders.rs.gov.br/pesquisa-ciptea):** Levantamento do Rio Grande do Sul sobre a situação escolar e laboral de pessoas com TEA.
* **[MEC e INEP - Censo Escolar 2023](https://www.gov.br/inep/pt-br/assuntos/noticias/censo-escolar/mec-e-inep-divulgam-resultados-do-censo-escolar-2023):** Dados nacionais sobre a educação.
* **[SciELO Brasil](https://www.scielo.br/j/ep/a/HmS58qB4qSGXLzsSRJzx43B/):** Impactos da política de educação especial (2008) no Ceará e em Fortaleza.
* **[Instituto Rodrigo Mendes - DIVERSA](https://diversa.org.br/noticias/conheca-os-modelos-de-atendimento-educacional-especializado-aee/):** Modelos de Atendimento Educacional Especializado (AEE).

---

## 🚀 Tecnologias e Estrutura

O projeto foi desenvolvido inteiramente em **Python** voltado para análise e visualização de dados.

**Estrutura do Repositório:**
* `data/` - Diretório contendo as bases de dados (arquivos CSV, planilhas, etc) utilizadas na análise.
* `modules/` - Módulos e funções auxiliares criadas para o tratamento e processamento dos dados.
* `views/` - Lógica de apresentação e geração das visualizações/gráficos.
* `app.py` - Arquivo principal para execução da aplicação ou painel de dados.
* `requirements.txt` - Lista de dependências e bibliotecas Python necessárias.

---

## 🔧 Como Instalar e Rodar Localmente

Siga os passos abaixo para configurar o ambiente e rodar o projeto na sua máquina:

### 1. Clonar o repositório
~~~bash
git clone https://github.com/AntDavid/educacao_e-_trabalho_de_pessoas_com_tea.git
cd educacao_e-_trabalho_de_pessoas_com_tea
~~~

### 2. Criar e ativar um ambiente virtual (Recomendado)
~~~bash
python -m venv venv

# Ativar no Windows:
venv\Scripts\activate

# Ativar no Linux/Mac:
source venv/bin/activate
~~~

### 3. Instalar as dependências
~~~bash
pip install -r requirements.txt
~~~

### 4. Executar a aplicação
~~~bash
python app.py
~~~
*(Dependendo da biblioteca utilizada, como Streamlit ou Dash, o comando pode variar para `streamlit run app.py` ou similar. Verifique a saída do terminal para acessar o link local).*

---

## 🎓 Sobre o PAIDEIA-LASSU

Este projeto foi desenvolvido como um trabalho de pesquisa do programa de formação **PAIDEIA**. 

O PAIDEIA é uma iniciativa de capacitação em tecnologia promovida pelo **LASSU** (Laboratório de Sustentabilidade em TIC) da **USP** (Universidade de São Paulo). O curso tem como foco preparar profissionais unindo o desenvolvimento de software e análise de dados com a sustentabilidade e o impacto social, aplicando conhecimentos teóricos em projetos reais e de grande relevância para a sociedade.

Conheça mais sobre a iniciativa: [LASSU-USP PAIDEIA](https://www.lassu.usp.br/paideia/)

---

## 📄 Licença

Projeto desenvolvido para fins educacionais, de pesquisa e portfólio.
