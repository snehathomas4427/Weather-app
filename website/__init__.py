#makes the website folder a python package

from flask import Flask

def create_app():
    app = Flask(__name__) #initializes flask
    app.config['SECRET_KEY'] = 'malu lol'

    #register blueprints
    from .views import views

    app.register_blueprint(views, url_prefix='/') #'/' means no prefix needed

    return app