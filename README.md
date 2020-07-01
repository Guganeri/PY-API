# PY-API 

**PY-API é uma API desenvolvida em Python/Flask.**

O dados utilizados por essa API são consumidos diretamente de [TheCatAPI](https://thecatapi.com/) armezena em um banco de dados (MongoDB) e disponibiliza atráves dos seguintes paths.

*PATHS:*

**O primeiro comando ao utilizar a API para popular o banco de dados.**  

[`localhost:5000`](http://localhost:5000) `/insert`


Listar todas as raças.

[`localhost:5000`](http://localhost:5000) `/listar-racas/` (`Listar todas as raças`)

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


