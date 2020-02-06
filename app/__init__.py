import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask (__name__)


app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'sqlite.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['Access-Control-Allow-Origin'] = '*'

db = SQLAlchemy(app)


from app.catalog.views import catalog
app.register_blueprint(catalog)

if not os.path.exists('sqlite:////' + os.path.join(basedir, 'sqlite.db')):
    db.create_all()