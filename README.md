# APLICAÇÃO RESTFUL API EM FLASK-RESTPLUS

## Inicio
 - Projeto desenvolvido em Python 3.6. Para que a aplicação possa rodar em servidores web, foram utlizadas as bibliotecas Flask e Flask Rest Plus.
 - Essa API utiliza um banco NoSQL MongoDB para armazenar dados de uma escola, criando uma collection curso contendo os campos: curso, materia, professor e horas.
 - A API insere, atualiza, deleta e pesquisa os dados no banco.
 - Utilizamos o Mongo-express para visualizar a banco de dados via web.

## Recursos utilizados no desenvolvimento:

- Flask;
- flask-restplus ~ v.0.13.0;
- pymongo ~ v.3.9.0;
- MongoDb;
- Mongo-express;
- PostMan (testar a API criada);


### Pré-requisitos
Todo o projeto foi adaptado para rodar em _containers_ do Docker. Então, para levantar a aplicação localmente é necessário ter instalado o [docker](https://docs.docker.com/install/) e o [docker-compose](https://docs.docker.com/compose/install/).  
```sh
user@usuer:/$ docker -v
Docker version 19.03.4, build 9013bf583a

user@usuer:/$ docker-compose -v
docker-compose version 1.24.1, build 4667896b
```
Depois de instalado é necessário construir as imagens docker das APIs do projeto.
```sh
user@usuer:/$ cd Mongo_CRUD/api
user@usuer:/Mongo_CRUD/api$ docker-compose build --parallel
```
É possível verificar se todas as images foram construídas com sucesso.  
As images **api_mongo_1**, **api_mongo-express_1** e **api_mongo_1**, devem aparecer no resultado da seguinte consulta:
```sh
user@usuer:/Mongo_CRUD/api$ docker image ls
```

### Iniciar a aplicação
Para o projeto  funcionar, é necessário subir os dockers. Para isso, basta levantar todos os containers através do ``docker-compose up``.
```sh
user@usuer:/Mongo_CRUD/api$ docker-compose up
```

#### Aplicações e seus endereços e portas
| API | Container | IP | Porta | Endereço |
| -- | -- | -- | -- | -- |
| API CRUD | api_mongo_crud_1 | localhost / 0.0.0.0 | 9001 | http://localhost:9001/swagger |
| MongoDB | mongo | localhost / 0.0.0.0 | 27017 | acessar por mongo-express http://localhost:8000/ |
| mongo-express | mongo-express | localhost / 0.0.0.0 | 8000 | http://localhost:8000/ |	

### Utilização
É possível testar a aplicação de 2 formas:
- Fazer requisições por Swagger: http://localhost:9001/swagger

- Enviar requisições no POSTMAN. 

## Testando a Aplicação no Postman:

Caso queira testar as API's criadas no projeto, primeiro baixe o [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop).
Depois de realizar o download do Postman, basta agora realizar os passos abaiaxo para 
poder testar cada API criada!

  ROTA                    |     HTTP(Verbo)   |      Descrição        | 
------------------------- | ----------------- | --------------------- | 
/mongo/search/all         |       GET         | Buscar todos os registros     | 
/mongo/search/curso/<string:curso>             |       GET        | Buscar registros pelo curso      | 
/mongo/search/materia/<string:materia>|       GET         | Buscar registros pela materia     | 
/mongo/insert |       POST         | Insere um novo registro     |    
/mongo/delete |       DELETE      | Excluir registro Por Id        |
/mongo/update |       PUT      | Atualiza registro Por Id        |

