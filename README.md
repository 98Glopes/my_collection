# My Collection API

API created in flask to save my collection of comics with goal to study the development: of RESTFull APIs. The app allow to register comic books in a Postgres database. The comic_book properties are:
* Name;
* Autor;
* Publisher;
* Description;

The available operations are:
* [Create a new register](#Create-a-new-register);
* Edit a register;
* Delete a register;
* View all registers;
* View a single register;

The system is online in a Heroku Server, and everybody can test it, available in: http://mycollectionapi.herokuapp.com/comic_books/

## Create a new register:

To create a new register is required to make a HTTP POST Request for the end point http://mycollectionapi.herokuapp.com/comic_books/ , the request needs a body with a JSON like right bellow:

``` javascript
{
        "autor": "Frank Miller",
        "description": "Writer/artist Frank Miller completely reinvents the legend of Batman...",
        "name": "Batman: The Dark",
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
