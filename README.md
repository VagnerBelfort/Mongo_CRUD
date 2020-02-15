# DILBERT - PREDIÇÃO DE SOLUÇÃO DE LOGS
Criar predição da melhor solução em logs de servidores.

## Inicio
Projeto desenvolvido em Python 3.6. Para que a aplicação possa rodar em servidores web, foram utlizadas as bibliotecas Flask e Flask Rest Plus. Já para a classifição e extração dos documentos enviados, estatística e técnicas de machine learning e deep learning foram utlizadas.

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
user@usuer:/$ cd dilbert/api_dilbert
user@usuer:/dilbert/api_dilbert$ docker-compose build --parallel
```
É possível verificar se todas as images foram construídas com sucesso.  
As images **01_predict_logs** e **02_client_dilbert**, devem aparecer no resultado da seguinte consulta:
```sh
user@usuer:/dilbert/api_dilbert$ docker image ls
```

### Iniciar a aplicação
Para o projeto DILBERT funcionar, é necessário que todas as suas APIs estejam de pé. Para isso, basta levantar todos os containers através do ``docker-compose up``.
```sh
user@usuer:/dilbert/api_dilbert$ docker-compose up
```

### Utilização
É possível testar a aplicação de 2 formas:
- Enviar aquivos através do _client_ (front-end).
- Enviar uma requisição POST para *predict_logs* como JSON contendo o  arquivo como base64. 
    ```json
    {
	"rotina": "GFID060",
	"programa": "GFIP0062",
	"logs": "888 *** GFIP0062 *** 25 - ERRO ABERTURA GFIF533E 888 *** GFIP0062 *** 25 - FILE STATUS 93 888 *** GFIP0062 *** 888 -CANCELADO"
    }
    ```

#### Aplicações e seus endereços e portas
| API | Container | IP | Porta | Endereço |
| -- | -- | -- | -- | -- |
| Cliente | 02_client_dilbert | localhost / 0.0.0.0 | 8012 | http://localhost:8012 |
| Predict Logs | 01_predict_logs | localhost / 0.0.0.0 | 9000 | http://localhost:9000/api/sol/ |


    
### Autores
- Vagner Menezes Belfort De Lima
- Arthur Rezende Bueno Pontes Barata

### Licença
Banco do Brasil S.A. (BB)
