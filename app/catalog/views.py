import json
from flask import request, jsonify, Blueprint, abort, make_response
from flask.views import MethodView
from app import db, app, cors
from app.catalog.models import ComicBook
from flask_cors import CORS, cross_origin

catalog = Blueprint('catalog', __name__)

@catalog.route('/')
@catalog.route('/home')
def home():
    return "welcome to the catalog home"



class ComicBookView(MethodView):

    def get(self, id=None, page=1):
        if not id:
            comic_books= ComicBook.query.paginate(page, 10).items
            res = []
            
            for comic in comic_books:
                res.append( {
                    'id': comic.id,
                    'name': comic.name,
                    'autor': comic.autor,
                    'publisher': comic.publisher,
                    'description': comic.description
                })
        else:
            comic = ComicBook.query.filter_by(id=id).first()
            if not comic:
                abort(404)
            res = {
                'id': comic.id,
                'name': comic.name,
                'autor': comic.autor,
                'publisher': comic.publisher,
                'description': comic.description
            }

        return jsonify(res)
    

    def post(self):
        req_data = request.get_json()
        name = req_data['name']
        autor = req_data['autor']
        publisher = req_data['publisher']
        description = req_data['description']
        comic = ComicBook(name, autor, publisher, description)
        db.session.add(comic)
        db.session.commit()

        payback = jsonify(
            {
                'id': comic.id,
                'name': comic.name,
                'autor': comic.autor,
                'publisher': comic.publisher,
                'description': description
            }            
        )
        return (payback, 201)


    def put(self, id):
        comic = ComicBook.query.filter_by(id=id).first()
        if not comic:
            abort(404)
        req_data = request.get_json()
        comic.name = req_data['name']
        comic.autor = req_data['autor']
        comic.publisher = req_data['publisher']
        comic.description = req_data['description']
        db.session.add(comic)
        db.session.commit()

        return jsonify(
            {
                'id': comic.id,
                'name': comic.name,
                'autor': comic.autor,
                'publisher': comic.publisher,
                'description': comic.description
            }
        )


    def delete(delf, id):
        comic = ComicBook.query.filter_by(id=id).first()
        if not comic:
            abort(404)
        db.session.delete(comic)
        db.session.commit()
        
        return jsonify(
            {
                'id': comic.id,
                'name': comic.name,
                'autor': comic.autor,
                'publisher': comic.publisher,
                'description': comic.description
            }
        )


comic_view = ComicBookView.as_view('comic_view')
app.add_url_rule(
    '/comic_books/', view_func=comic_view, methods=['GET', 'POST'],
)
app.add_url_rule(
    '/comic_books/<int:id>/', view_func=comic_view, methods=['GET', 'PUT', 'DELETE'],
)

