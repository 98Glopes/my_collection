import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask (__name__)


app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://kcvktcfoyswdpi:75362912a7624ad5fc303836733ffb867cf1e4c1fa0a8baa05cfa8df283545e5@ec2-3-213-192-58.compute-1.amazonaws.com:5432/dcnf0af9aa6l8c'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['Access-Control-Allow-Origin'] = '*'

db = SQLAlchemy(app)


from app.catalog.views import catalog
app.register_blueprint(catalog)

