import pandas as pd

# Função para carregar dados
def load_data(file_path):
    return pd.read_csv(file_path)

# Carregar dados
def read_database(load_data):
    situacao_escolar = load_data('../data/situacao_escolar.csv')
    nivel_escolarizacao = load_data('../data/nivel_escolarizacao.csv')
    idade_trabalho = load_data('../data/idade_trabalho.csv')
    trabalho_cotas = load_data('../data/trabalho_cotas.csv')
    municipios_instituicoes = load_data('../data/municipios_instituicoes.csv')
    
    return {
        "situacao escolar": situacao_escolar,
        "nivel escolarizacao": nivel_escolarizacao,
        "idade trabalho": idade_trabalho,
        "trabalho cotas": trabalho_cotas,
        "municipios instituicoes": municipios_instituicoes
    }
