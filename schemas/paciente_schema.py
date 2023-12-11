from pydantic import BaseModel
from typing import Optional, List
from model.paciente import Paciente
import json
import numpy as np

from pydantic import BaseModel

class PacienteSchema(BaseModel):
    """ Define como um novo paciente a ser inserido deve ser representado
    """
    name: str = "Tadeu"
    age: int = 44	
    sex: int = 1
    cp: int = 2
    trestbps: int = 130
    chol: int = 233
    fbs: int = 0
    restecg: int = 1
    thalach: int = 179
    exang: int = 1
    oldpeak: float = 0.4
    slope: int = 2
    ca: int = 0
    thal: int = 2
    
    
class PacienteViewSchema(BaseModel):
    """Define como um paciente será retornado
    """
    id: int = 1
    name: str = "Maria"
    age: int = 52	
    sex: bool = 0
    cp: int = 0
    trestbps: int = 125
    chol: int = 212
    fbs: bool = 0
    restecg: int = 1
    thalach: int = 168
    exang: bool = 0
    oldpeak: float = 1.0
    slope: int = 2
    ca: int = 2
    thal: int = 3
    outcome: int = None

class PacienteBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do paciente.
    """
    name: str = "Maria"


class ListaPacientesSchema(BaseModel):
    """Define como uma lista de pacientes será representada
    """
    pacientes: List[PacienteSchema]


class PacienteDelSchema(BaseModel):
    """Define como um paciente para deleção será representado
    """
    name: str = "Maria"
    
# Apresenta apenas os dados de um paciente    
def apresenta_paciente(paciente: Paciente):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    return {
        "id": paciente.id,
        "age": paciente.age,
        "sex": paciente.sex,
        "cp": paciente.cp,
        "trestbps": paciente.trestbps,
        "chol": paciente.chol,
        "fbs": paciente.fbs,
        "restecg": paciente.restecg, 
        "thalach": paciente.thalach, 
        "exang": paciente.exang, 
        "oldpeak": paciente.oldpeak, 
        "slope": paciente.slope, 
        "ca": paciente.ca, 
        "thal": paciente.thal, 
        "outcome": paciente.outcome 
    }
    
# Apresenta uma lista de pacientes
def apresenta_pacientes(pacientes: List[Paciente]):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    result = []
    for paciente in pacientes:
        result.append({
            "id": paciente.id,
            "name": paciente.name,
            "age": paciente.age,
            "sex": paciente.sex,
            "cp": paciente.cp,
            "trestbps": paciente.trestbps,
            "chol": paciente.chol,
            "fbs": paciente.fbs,
            "restecg": paciente.restecg, 
            "thalach": paciente.thalach, 
            "exang": paciente.exang, 
            "oldpeak": paciente.oldpeak, 
            "slope": paciente.slope, 
            "ca": paciente.ca, 
            "thal": paciente.thal, 
            "outcome": paciente.outcome 
        })

    return {"pacientes": result}