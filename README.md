# My Collection API

API created in flask to save my collection of comics with goal to study the development: of RESTFull APIs. The app allow to register comic books in a Postgres database. The comic_book properties are:
* Name;
* Autor;
* Publisher;
* Description;

The available operations are:
* [Create a new register](#Create-a-new-register);
* [Edit a register](#Edit-a-register);
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

## Edit a register
 
To edit any register is required the objects Id, so is necessary make a HTTP PUT request to the endpoint: http://mycollectionapi.herokuapp.com/comic_books/<int:id>. The request need a JSON with the new object's content, like the New Register case. By example:
``` javascript
// PUT request to endpoint http://mycollectionapi.herokuapp.com/comic_books/29/

{
        "autor": "Frank Miller & Klauss Janson",
        "description": "Writer/artist Frank Miller completely reinvents the legend of Batman...",
        "name": "Batman: The Dark",
        "publisher": "DC Comis"
    }
```
The response will be a HTTP response code 200 and a JSOM with the new content of the object:
``` javascript
{
  "autor": "Frank Miller & Klauss Janson",
  "description": "Writer/artist Frank Miller completely reinvents the legend of Batman...",
  "id": 29,
  "name": "Batman: The Dark",
  "publisher": "DC Comis"
}
```
If the Id's passed on the URL doesn't exist, the API will return an 404 error code.


