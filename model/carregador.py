import pandas as pd
from logger import logger

class Carregador:

    def carregar_dados(self, url: str):
        """ Carrega e retorna um DataFrame. Há diversos parâmetros 
        no read_csv que poderiam ser utilizados para dar opções 
        adicionais.
        """
        dataset = pd.read_csv(url, delimiter=',')

        # Alterando retorno, onde: Beligno: 0 | Maligno: 1
        dataset['diagnosis'] = dataset['diagnosis'].map({'B': 0, 'M': 1})

        # Selecionando apenas as colunas essenciais
        colunas_especificas = ['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
               'compactness_mean', 'concavity_mean', 'concave points_mean', 'symmetry_mean',
               'fractal_dimension_mean', 'diagnosis']

        dataset = dataset[colunas_especificas]
        
        return dataset
    