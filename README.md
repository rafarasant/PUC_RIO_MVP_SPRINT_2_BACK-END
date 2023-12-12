# Sistema de Diagnóstico de Doenças Cardíacas (SDDC) - APP FRONT-END 

O **Sistema de Diagnóstico de Doenças Cardíacas (SDDC)** busca prover aos profissionais médicos 
uma ferramenta auxiliar para o diagnóstico de doenças cardíacas.

No presente projeto, o SDDC é empregado no contexto de um consultório especializado em cardiologia, cujos serviços são 
prestados por um único profissional cardiologista. Cabe ao médico o uso dessa ferramenta para cadastrar os dados de seus
pacientes e verificar se eles portam, ou não, uma doença cardíaca. 

Para que seja possível a realização desse diagnóstico, a aplicação emprega o modelo de aprendizagem de máquina (*machine learning*) 
*Decision Tree Classifier*, o qual é capaz de retornar, com base nos dados médicos fornecidos, os valores "0" (para a ausência de doença
cardíaca) ou "1" (para a presença de doença cardíaca).

Os resultados de cada diagnóstico podem ser verificados de duas formas: a primeira é através do Swagger, por meio da execução 
das rotas POST ou GET, onde o valor do resultado constará no parâmetro *outcome*. Já a segunda é mediante o acesso
à página *web* da aplicação, correspondente ao seu front-end.

Para maiores detalhes, leia os tópicos a seguir.

>Importante: no último tópico deste arquivo (tópico 8), deixo os links (Google Drive e YouTube) para um vídeo contendo a apresentação do meu projeto.

Este projeto foi desenvolvido para o MVP da Sprint 2 da **Pós Gradução de Engenharia de Softwarer da PUC-Rio**. 
<br>
---
<br>
## Execução da aplicação

Para executar esta aplicação, siga os passos enumerados a seguir:


### 1 - Clone o repositório

Clone o repositório através do comando abaixo:

```
[git clone (...)](https://github.com/rafarasant/PUC_RIO_MVP_SPRINT_2_BACK-END.git)
```


### 2 - Instale as dependências

Para que seja possível executar a aplicação, é preciso instalar primeiramente todas as *libs* (bibliotecas) listadas no arquivo *requirements.txt*. 
Isso deve ser feito no diretório raiz, através do terminal, a partir do seguinte comando.

> Importante: recomença-se fortemente o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

> Atenção: O símbolo *(env)$* presente nos comandos abaixo refere-se tão somente a um exemplo de ambiente virtual ativado. Contudo, não faz por parte dos comandos em si.

```
(env)$ pip install -r requirements.txt
```


### 3 - Execute a API

No terminal, execute o comando abaixo (certifique-se de que a porta 5000 está sendo usada para este projeto):

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Caso esteja em modo de desenvolvimento, recomenda-se executar o comando acima junto do parâmetro *reload*, o qual reinicia o servidor automaticamente
após qualquer alteração no código fonte.

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```


### 4 - Banco de dados

A pasta *database*, localizada na raiz do projeto, contém o arquivo *pacientes.sqlite3*. Nela já se encontra criada a tabela necessária para a execução da API.


### 5 - Documentação da API no navegador (Swagger)

No navegador, abra o link abaixo para visualizar o status da API em execução. 

```
localhost:5000/
```


### 6 - Página *Web*

Para executar a aplicação através da página *web*, primeiramente crie uma pasta no diretório raíz e cole nela os arquivos do front-end da aplicação,
os quais podem ser acessados neste repositório:

```
https://github.com/rafarasant/PUC_RIO_MVP_SPRINT_2_FRONT-END.git
```

Em seguida, sirva a aplicação conforme explicado no item 3 (acima). Depois, copie o caminho absoluto (*path*) do arquivo Index.html e cole-o na barra
de pesquisa do navegador. Após essas etapas, será possível visualizar a página *web*, na qual constará uma tabela contendo todos os dados dos 
pacientes cadastrados no banco de dados.


### 7 - Pytest

No presente repositório, ainda estão presentes os dois arquivos referentes ao teste do modelo de aprendizagem de máquina e do *dataset*. No arquivo *main_test_model.py* se encontram as funções principais do teste, as quais estatipulam como devem ser calculadas as métricas usadas na avaliação do *modelo* e do *dataset* escolhidos. Por exemplo, a função *get_acc()* prevê o cálculo a acurácia do modelo empregado. Já no arquivo *test_model.py* estão as funções que possuem o comando *assert*, para verificar se as métricas, umas vez calculadas, possuem o valor esperado.

Para a execução do teste, abra o terminal e, no diretório raíz, execute o seguinte comando:

```
pytest test_model.py
```


### 8 - Vídeo de apresentação do projeto

O vídeo contendo a apresentação do meu projeto pode ser acessado através de um dos seguintes links:

```
https://drive.google.com/drive/folders/1tGbvZtc1ywzQEW6oITPLeeXdHnEohV8V?usp=drive_link
```

```
https://youtu.be/iKXd2Xm7F-Q
```
