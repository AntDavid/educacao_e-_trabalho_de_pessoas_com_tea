import pandas as pd
import os

# Função para carregar dados
def load_data(file_path):
    
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    abs_path = os.path.join(parent_dir, 'data', file_path)
    if not os.path.isfile(abs_path):
        raise FileNotFoundError(f"O arquivo não foi encontrado: {abs_path}")
    return pd.read_csv(abs_path)


# Carregar dados
def read_database():
    situacao_escolar = load_data('situacao_escolar.csv')
    nivel_escolarizacao = load_data('nivel_escolarizacao.csv')
    idade_trabalho = load_data('idade_trabalho.csv')
    trabalho_cotas = load_data('trabalho_cotas.csv')
    municipios_instituicoes = load_data('municipios_instituicoes.csv')
    
    return {
        "situacao escolar": situacao_escolar,
        "nivel escolarizacao": nivel_escolarizacao,
        "idade trabalho": idade_trabalho,
        "trabalho cotas": trabalho_cotas,
        "municipios instituicoes": municipios_instituicoes
    }
