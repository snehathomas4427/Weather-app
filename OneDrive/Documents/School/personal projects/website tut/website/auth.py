from flask import Blueprint
#blueprint - has a bunch of roots inside of it and urls here

auth = Blueprint('auth',__name__)  #naming this the same as ur file/variable keeps it simple

@auth.route('/login')
def login():
  return "<p>Login</p>"

@auth.route('/logout')
def logout():
  return "<p>logout</p>"

@auth.route('/sign-up')
def sign_up():
  return "<p> Sign up </p>"