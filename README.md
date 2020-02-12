# My Collection API

API created in flask to save my collection of comics with goal to study the development: of RESTFull APIs. The app allow to register comic books in a Postgres database. The comic_book properties are:
* Name;
* Autor;
* Publisher;
* Description;

The available operations are:
* [Create a new register](#Create-a-new-register);
* [Edit a register](#Edit-a-register);
* [Delete a register](#Delete-a-register);
* [View all registers]("View-all-register);
* [View a single register](#View-a-single-register);

The system is online in a Heroku Server, and everybody can test it, available in: http://mycollectionapi.herokuapp.com/comic_books/

I'm building an site to consume my API, this site use HTML, CSS an JS. The source code is available the [my_collection_frontend repositorie](https://github.com/98Glopes/my_collection_frontend). The site is available to in [My Collection Github Pages](https://98glopes.github.io/my_collection_frontend/index.html). I've a [to do list](#To-do-list) with future improvements.


## Create a new register:

To create a new register is required to make a HTTP POST Request for the end point http://mycollectionapi.herokuapp.com/comic_books/ , the request needs a body with a JSON like right bellow:

``` javascript
{
        "autor": "Frank Miller",
        "description": "Writer/artist Frank Miller completely reinvents the legend of Batman...",
        "name": "Batman: The Dark",y_
        "publisher": "DC Comis"
    }
```
The response of the request will be HTTP code 201 and a JSON with the object created including the New Object's Id:
``` javascript
{
    "autor": "Frank Miller",
    "description": "Writer/artist Frank Miller completely reinvents the legend of Batman...",
    "id": 29,
    "name": "Batman: The Dark",
    "publisher": "DC Comis"
}
```
That id can be used in the others API's resources.

## Edit a register
 
To edit any register is required the objects Id, so is necessary make a HTTP PUT request to the endpoint: http://mycollectionapi.herokuapp.com/comic_books/[int:id]. The request need a JSON with the new object's content, like the New Register case. By example:
``` javascript
// PUT request to endpoint http://mycollectionapi.herokuapp.com/comic_books/29/

{
        "autor": "Frank Miller & Klauss Janson",
        "description": "Writer/artist Frank Miller completely reinvents the legend of Batman...",
        "name": "Batman: The Dark",
        "publisher": "DC Comis"
    }
```
The response will be a HTTP response code 200 and a JSON with the new content of the object:
``` javascript
{
  "autor": "Frank Miller & Klauss Janson",
  "description": "Writer/artist Frank Miller completely reinvents the legend of Batman...",
  "id": 29,
  "name": "Batman: The Dark",
  "publisher": "DC Comis"
}
```
If the Id passed on the URL doesn't exist, the API will return an 404 error code.

## Delete a register

To delete a register is necessary a HTTP DELETE request to the endpoint http://mycollectionapi.herokuapp.com/comic_books/[int:id]with the Id of the object we want delete. In that case, no JSON body is needed. In the susscesfuly case, the API will return a JSON with the deleted object:
``` javascript
{
  "autor": "Frank Miller & Klauss Janson",
  "description": "Writer/artist Frank Miller completely reinvents the legend of Batman...",
  "id": 29,
  "name": "Batman: The Dark",
  "publisher": "DC Comis"
}
```
If the Id doesn't exist on the database, the API will return an 404 error code.

## View all register

To view all the register in the database is necessary a HTTP GET request to the endpoint http://mycollectionapi.herokuapp.com/comic_books/ . No JSON Body is needed in that case, the response will be a JSON list with all the comic books registered in the API:
``` javascript
[
  {
    "autor": "Marcelo Quintanilha ",
    "description": "Baseado em Dostoiévski ",
    "id": 3,
    "name": "Talco de Vidro",
    "publisher": "Veneta"
  },
  {
    "autor": "Marcelo D'Salete",
    "description": "Angola Janga, “pequena Angola” ou, como dizem os livros de história, Palmares. Por mais de cem anos, foi como um reino africano dentro da América do Sul. E, apesar do nome, não tão pequeno: Macaco, a capital de Angola Janga, tinha uma população equivalente a das maiores cidades brasileiras da época.Formada no fim do século XVI, em Pernambuco, a partir dos mocambos criados por fugitivos da escravidão, Angola Janga cresceu, organizou-se e resistiu aos ataques dos militares holandeses e das forças coloniais portuguesas. Tornou-se o grande alvo do ódio dos colonizadores e um símbolo de liberdade para os escravizados. ",
    "id": 4,
    "name": "Angola Janga",
    "publisher": "Veneta"
  },
  {
    "autor": "Art Spiegelman",
    "description": "Maus (\"rato\", em alemão) é a história de Vladek Spiegelman, judeu polonês que sobreviveu ao campo de concentração de Auschwitz, narrada por ele próprio ao filho Art. O livro é considerado um clássico contemporâneo das histórias em quadrinhos. Foi publicado em duas partes, a primeira em 1986 e a segunda em 1991",
    "id": 5,
    "name": "Maus",
    "publisher": "Quadrinhos na Cia."
  }
}
]
```
At the moment, the API only return first 10 registers in database by debuging reasons.

## View a single register

To view a single register is necessary do a HTTP GET resquest to the endpoint http://mycollectionapi.herokuapp.com/comic_books/[int:id] with the Id register. No JSON body is needed in that case. The response will be a JSON with de register content, if the id doesn't exist the API will return a 404 error code. A response example can see bellow:
``` javascript
{
  "autor": "Marcelo Quintanilha ",
  "description": "Baseado em Dostoiévski ",
  "id": 3,
  "name": "Talco de Vidro",
  "publisher": "Veneta"
}
``` 

## To do list:

* Implent JWT authentication;
* Improve the HTTP response codes;
* Reject requests without the Header: Content-Type:application/json

