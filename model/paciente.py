from sqlalchemy import Column, String, Integer, DateTime, Float, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

# colunas = Name, Age, Sex, ChestPaint, ResringBloodPressure, SerumCholestorol, FastingBloodSugar, ElectrocardiographicResults,
#  MaximumHeartRateAchieved, ExerciseInducedAngina, Oldpeak, Slope, ColoredVesselsNumber, Talassemia, Diagnostic

class Paciente(Base):
    __tablename__ = 'pacientes'

    id = Column(Integer, primary_key=True)
    name = Column("Name", String(50))
    age = Column("Age", Integer)
    sex = Column("Sex", Integer)
    cp = Column("ChestPain", Integer)
    trestbps = Column("RestingBloodPressure", Integer)
    chol = Column("SerumCholestorol", Integer)
    fbs = Column("FastingBloodSugar", Integer)
    restecg = Column("ElectrocardiographicResults", Integer)
    thalach = Column("MaximumHeartRateAchieved", Integer)
    exang = Column("ExerciseInducedAngina", Integer)
    oldpeak = Column("Oldpeak", Float)
    slope = Column("Slope", Integer)
    ca = Column("NumberOfColoredVessels", Integer)
    thal = Column("Talassemia", Integer)
    outcome = Column("Diagnostic", Integer, nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())
        
        
    def __init__(self, name:str, age:int, sex:int, cp:int,
                 trestbps:int, chol:int, fbs:int, restecg:int,
                 thalach:int, exang:int, oldpeak:float, slope:int,
                 ca:int, thal:int, outcome:int,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Paciente

        Arguments:
        name: nome do paciente
            age: idade
            sex: sexo do paciente
            cp: tipo de dor no peito
            trestbps: pressão sanguínea em repouso
            chol: colesterol sérico
            fbs: Açúcar no sangue em jejum
            restecg: Resultados eletrocardiográficos em repouso
            thalach: Frequência cardíaca máxima atingida
            exang: Angina induzida por exercício
            oldpeak: Depressão de ST induzida por exercício em relação ao repouso
            slope: Inclinação do segmento ST de pico do exercício
            ca: Número de vasos principais coloridos por fluoroscopia
            thal: Talassemia
            outcome: diagnóstico
            data_insercao: data de quando o paciente foi inserido à base
        """
        self.name = name
        self.age = age
        self.sex = sex
        self.cp = cp
        self.trestbps = trestbps
        self.chol = chol
        self.fbs = fbs
        self.restecg = restecg
        self.thalach = thalach
        self.exang = exang
        self.oldpeak = oldpeak
        self.slope = slope
        self.ca = ca
        self.thal = thal
        self.outcome = outcome

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao