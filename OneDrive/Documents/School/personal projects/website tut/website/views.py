from flask import Blueprint, render_template
#blueprint - has a bunch of routes inside of it and urls here

views = Blueprint('views',__name__)  #naming this the same as ur file/variable keeps it simple

@views.route('/')
def home(): #this function will run whenever we go to /route
  

  return render_template("home.html")

