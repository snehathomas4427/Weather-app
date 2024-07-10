#stores the URL endpoints/routes (ex: login page, home page, etc.) t

from flask import Blueprint, render_template, request, flash
from weather import main as get_weather

#blueprint allows you create routes in different files
views = Blueprint('views' , __name__)

#to define a route:
@views.route('/', methods=['GET', 'POST']) #for the home page. this function will run whenever we go to the '/' route 
def home():
    data = None
    if request.method == "POST":
        #what to do if location isn't valid???? time stamp: 1:03:00
        #if len(location) < 2:
            #flash("No Results Found", category='error')

        city = request.form.get('city')
        state = request.form.get('state')
        country = request.form.get('country')
        data = get_weather(city, state, country)
        if data == None:
            flash("No Results Found", category='error')

    return render_template('base.html', data=data) #This line renders the base.html template and passes the data variable to the template. The data variable can be used within the template to display the fetched weather information.

@views.route('/hourly')
def hourly():
    return render_template('hourly.html')

@views.route('/tenday')
def tenday():
    return render_template('tenday.html')