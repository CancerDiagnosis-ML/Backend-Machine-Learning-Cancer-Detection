import pandas as pd

class Carregador:

    def carregar_dados(self, url: str, atributos: list):
        """ Carrega e retorna um DataFrame. Há diversos parâmetros 
        no read_csv que poderiam ser utilizados para dar opções 
        adicionais.
        """
        
        dataset = pd.read_csv(url, names=atributos, delimiter=',')
        
        # Mapeia 'B' para 0 e 'M' para 1 na coluna 'diagnosis'
        dataset['diagnosis'] = dataset['diagnosis'].map({'B': 0, 'M': 1})
        
        return dataset
    