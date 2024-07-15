#stores the URL endpoints/routes (ex: login page, home page, etc.) t

from flask import Blueprint, render_template, request, flash, session
from weather import main_current_weather as get_weather
from weather import main_daily_weather as daily_weather
from weather import main_hourly_weather as hourly_weather

#blueprint allows you create routes in different files
views = Blueprint('views' , __name__)

#to define a route:
@views.route('/', methods=['GET', 'POST']) #for the home page. this function will run whenever we go to the '/' route 
def home():
    data = None
    city = None
    state = None
    if request.method == "POST":
        #what to do if location isn't valid???? time stamp: 1:03:00
        #if len(location) < 2:
            #flash("No Results Found", category='error')

        city = request.form.get('city')
        state = request.form.get('state')
        country = request.form.get('country')

        #if city or state or country 
        if not city or not state or not country:
            flash("Please provide a valid city, state, and country.", category='error')
        else:
            data = get_weather(city, state, country)
            if data == None:
                flash("No Results Found", category='error')
            else:
                session['city'] = city
                session['state'] = state
                session['country'] = country

    return render_template('base.html', data=data, city=city, state=state) #This line renders the base.html template and passes the data variable to the template. The data variable can be used within the template to display the fetched weather information.

@views.route('/hourly', methods=['GET', 'POST'])
def hourly():
    data = None
    city = None
    state = None
    city = session.get('city')
    state = session.get('state')
    country = session.get('country')
    if city and state and country:
        data = hourly_weather(city, state, country)

    return render_template('hourly.html', data=data, city=city, state=state)

@views.route('/tenday', methods=['GET', 'POST'])
def tenday():
    data = None
    city = None
    state = None
    city = session.get('city')
    state = session.get('state')
    country = session.get('country')
    if city and state and country:
        data = daily_weather(city, state, country)
    
    return render_template('tenday.html', data=data, city=city, state=state)

@views.route('/map', methods=['GET', 'POST'])
def map():
    data=None

    return render_template('map.html')