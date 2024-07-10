#makes the website folder a python package

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__) #initializes flask
    app.config['SECRET_KEY'] = 'asdf fadsf'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    db.init_app(app) 

    #register blueprints
    from .views import views

    app.register_blueprint(views, url_prefix='/') #'/' means no prefix needed

    return app