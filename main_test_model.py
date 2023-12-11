# Imports necessários
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from model import Model

np.random.seed(7) # definindo uma semente global

# Referência ao Dataset
dataset_url = "database/dataset_200_pytest.csv"

# Lê o arquivo
dataset = pd.read_csv(dataset_url, delimiter=',')

# Transforma o dataset em uma lista
array = dataset.values

X = array[:,0:13]

# Seleciona apenas os elementos da coluna 'outcome'
Y = array[:,13]

# Carregamento do modelo

ml_path = 'ml_model/heart_disease_3.pkl'

modelo = Model.carrega_modelo(ml_path)

# Realiza predição dos resultados com base no modelo
prediction = modelo.predict(X)

class Dataset:

    # def getNoe() -> int:
    def getNoe():
        """Verifica o número total de elementos(noe)
        registados no dataset.
        """
        
        get_noe = len(X)
        return get_noe

    # def getPop() -> float:
    def getPop():
        """Verifica o percentual de resultados (outcomes)
        positivos registrados no dataset. Isto é, quando 
        o valor de 'outcome' == 1.
        """

        positive_outcomes = []

        for y in Y:
            if y == 1:
                positive_outcomes.append(y)

        get_npo = len(positive_outcomes)
        get_pop = get_npo / len(Y)
        return get_pop
    

class TestModel:

    # def get_acc() -> float:
    def get_acc():
        """Verifica o valor da acurácia do model.
        """

        accuracy = accuracy_score(Y, prediction)
        return accuracy
    
    # def get_recall() -> float:
    def get_recall():
        """Verifica o valor de 'recall' do model.
        """

        recall = recall_score(Y, prediction, average='binary')
        return recall
    
    # def get_precision() -> float:
    def get_precision():
        """Verifica o valor de precisão do model.
        """

        precision = precision_score(Y, prediction, average='binary')
        return precision

    # def f1_score() -> float:
    def f1_score():          
        """Verifica o valor de "f1_score" do model.
        """
        
        f1 = f1_score(Y, prediction, average='binary')
        return f1
    