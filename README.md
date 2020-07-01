# PY-API 

**PY-API é uma API desenvolvida em Python/Flask.**

O dados utilizados por essa API são consumidos diretamente de [TheCatAPI](https://thecatapi.com/) armezena em um banco de dados (MongoDB) e disponibiliza através dos seguintes paths.

### PATHS:

**O primeiro comando ao utilizar a API para popular o banco de dados.**  

[`localhost:5000`](http://localhost:5000) `/insert`


Listar todas as raças.

[`localhost:5000`](http://localhost:5000) `/listar-racas/` 

Listar informações partindo de uma raça.

[`localhost:5000`](http://localhost:5000) `/listar-racas/{digitarRaca}/`

Listar raças partindo de um temperamento.

[`localhost:5000`](http://localhost:5000) `'/listar-racas/temperamento/{digitarTemperamento}/'`

Listar raças partindo de uma origem

[`localhost:5000`](http://localhost:5000) `/listar-racas/origem/{digitarOrigem}/`

Listar imagem de gatos com chapéu.

[`localhost:5000`](http://localhost:5000) `/listar/img/chapeu/`

Listar imagem de gatos com óculus.

[`localhost:5000`](http://localhost:5000) `/listar/img/oculus/`

## Uso:

1. Local

    ``` 
    Clone o repositório: https://github.com/Guganeri/PY-API
    ```

    ``` 
    cd src
    cria um arquivo chamado '.env' e dentro dele adicione as linhas: 

    URL=https://api.thecatapi.com/v1
    TOKEN='SEU-TOKEN-THECATAPI'
    BDURL='URL-MONGODB'
    ```

    ```
    Execute: pip3 install -r requirements.txt or pip install -r requirements.txt
    ```

    ```
    Execute: python3 app.py
    ```

    **Se você estiver usando OS Windows será necessário alterar a última linha do arquivo app.py de host="0.0.0.0" para host="127.0.0.1"**


2. Docker

    ```
    sudo docker run -d --restart=unless-stopped -p 5000:5000 \
    --env="URL=https://api.thecatapi.com/v1" \
    --env="DBURL=MongoDbUrl" \
    --env="TOKEN=SuaApiKey" \
    guganeri/apicatpy:v1
    ```
## Requisitos:

- [x] Python: 3.7
- [x] Pip: 20.0.2
- [x] MongoDB
- [x] Git

## DockerHub:

- [PY-API](https://hub.docker.com/repository/docker/guganeri/apicatpy)