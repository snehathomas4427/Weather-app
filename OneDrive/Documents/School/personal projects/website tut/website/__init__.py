from flask import Flask

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'shadow puppy'

  from .views import views
  from .auth import auth   #importing blueprints

  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')  #'/' means no prefix

  return app


