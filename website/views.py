#stores URL endpoints for the frontend part of the website
#stores the routes (ex: login page, home page, etc.) t

from flask import Blueprint, render_template

views = Blueprint('views' , __name__)

#to define a route:
@views.route('/') #for the home page. this function will run whenever we go to the '/' route 
def home():
    return render_template('home.html')

@views.route('/today')
def today():
    return render_template('today.html')

@views.route('/tenday')
def tenday():
    return render_template('tenday.html')