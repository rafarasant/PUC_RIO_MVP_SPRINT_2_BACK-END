from flask_openapi3 import OpenAPI, Info, Tag

from flask import redirect, request
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Paciente, Model
# from logger import logger
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
paciente_tag = Tag(name="Paciente", description="Adição, visualização, remoção e predição de pacientes com Diabetes")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rota de listagem de pacientes
@app.get('/pacientes', tags=[paciente_tag],
         responses={"200": PacienteViewSchema, "404": ErrorSchema})
def get_pacientes():
    """Lista todos os pacientes cadastrados na base
    Retorna uma lista de pacientes cadastrados na base.
    
    Args:
        nome (str): nome do paciente
        
    Returns:
        list: lista de pacientes cadastrados na base
    """
    session = Session()
    import os
    current_path = os.getcwd()

    print(f"Current path: {current_path}")
    # Buscando todos os pacientes
    pacientes = session.query(Paciente).all()
    
    if not pacientes:
        # logger.warning("Não há pacientes cadastrados na base :/")
        return {"message": "Não há pacientes cadastrados na base :/"}, 404
    else:
        # logger.debug(f"%d pacientes econtrados" % len(pacientes))
        return apresenta_pacientes(pacientes), 200


# Rota de adição de paciente
@app.post('/paciente', tags=[paciente_tag],
          responses={"200": PacienteViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: PacienteSchema):
    """Adiciona um novo paciente à base de dados
    Retorna uma representação dos pacientes e diagnósticos associados.
    
    Args:

        name (str): nome do paciente 
        age (int): idade (anos): Age
        sex (boolean): sexo do paciente | 0 = feminino, 1 = masculino : sex
        cp (int): tipo de dor no peito (4 valores) : Chest pain type
        trestbps (int): pressão sanguínea em repouso (mmHg - milimetros de mercúrio) : Resting blood pressure
        chol (int) : colesterol sérico em (mg/dl - miligramas por decilitro) : serum cholestorol 
        fbs (boolean) : Açúcar no sangue em jejum > 120 mg/dl = 0 | < 120mg/dl = 1 : fasting blood sugar 
        restecg (int) : Resultados eletrocardiográficos em repouso (valores 0, 1, 2) : resting electrocardiographic results
        thalach (int) : Frequência cardíaca máxima atingida (bpm - batimentos por minuto) : maximum heart rate achieved
        exang (boolean) : Angina induzida por exercício : exercise induced angina | 1 = sim, 1 = não
        oldpeak (float) : Depressão de ST induzida por exercício em relação ao repouso : ST depression induced by exercise relative to rest
        slope (int) : Inclinação do segmento ST de pico do exercício : the slope of the peak exercise ST segment
        ca (int) : Número de vasos principais coloridos por fluoroscopia (0-3) : number of major vessels (0-3) colored by flouroscopy
        thal (int) : Talassemia: 1 = normal; 2 = problema corrigido; 3 = problema reversível
        
    Returns:
        dict: representação do paciente e diagnóstico associado
    """
    
    # Carregando modelo

    # ----------------------------------------------------------------
    ml_path = 'ml_model/heart_disease_3.pkl'
    
    
    modelo = Model.carrega_modelo(ml_path)
    # ----------------------------------------------------------------


    paciente = Paciente(
              
        name=request.form["name"],
        age=request.form["age"],
        sex=request.form["sex"],
        cp=request.form["cp"],
        trestbps=request.form["trestbps"],
        chol=request.form["chol"],
        fbs=request.form["fbs"],
        restecg=request.form["restecg"],
        thalach=request.form["thalach"],
        exang=request.form["exang"],
        oldpeak=request.form["oldpeak"],
        slope=request.form["slope"],
        ca=request.form["ca"],
        thal=request.form["thal"],
        outcome=Model.preditor(modelo, form)
    )
    # logger.debug(f"Adicionando produto de nome: '{paciente.name}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se paciente já existe na base
        if session.query(Paciente).filter(Paciente.name == request.form["name"]).first():
            error_msg = "Paciente já cadastrado na base :/"
            # logger.warning(f"Erro ao adicionar paciente '{paciente.name}', {error_msg}")
            return {"message": error_msg}, 409
        
        # Adicionando paciente
        session.add(paciente)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        # logger.debug(f"Adicionado paciente de nome: '{paciente.name}'")
        return apresenta_paciente(paciente), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        # logger.warning(f"Erro ao adicionar paciente '{paciente.name}', {error_msg}")
        return {"message": error_msg}, 400
   
    
# Rota de remoção de paciente por nome
@app.delete('/paciente', tags=[paciente_tag],
            responses={"200": PacienteViewSchema, "404": ErrorSchema})
def delete_paciente(query: PacienteBuscaSchema):
    """Remove um paciente cadastrado na base a partir do nome

    Args:
        nome (str): nome do paciente
        
    Returns:
        msg: Mensagem de sucesso ou erro
    """
    
    paciente_nome = unquote(query.name)
    # logger.debug(f"Deletando dados sobre paciente #{paciente_nome}")
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando paciente
    paciente = session.query(Paciente).filter(Paciente.name == paciente_nome).first()
    
    if not paciente:
        error_msg = "O paciente não está cadastrado na base :/"
        # logger.warning(f"Erro ao deletar paciente '{paciente_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(paciente)
        session.commit()
        # logger.debug(f"Deletado paciente #{paciente_nome}")
        return {"message": f"Paciente {paciente_nome} removido com sucesso."}, 200