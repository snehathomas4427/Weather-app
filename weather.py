import requests
from datetime import datetime
from dataclasses import dataclass

api_key = 'ff13222f452ad448227993242c3afbec'
new_key = '1488dff0c0434ab2951212603241307'

@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temp: float
    temp_max: float
    temp_min: float

@dataclass
class DailyData:
    #time: float
    date: str
    description: str
    #temp: int
    icon: str
    temp_max: int
    temp_min: int
    precipitation: int

@dataclass
class HourlyData:
    time: float
    temp: int
    icon: str
    description: str

def get_lat_lon(city_name, state_code, country_code, api_key):

    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={api_key}').json()
    if not resp: #if resp is empty
        return None, None
    lat, lon = resp[0]['lat'], resp[0]['lon']
    return lat,lon

#print(get_lat_lon('Orlando', 'FL', 'US', api_key))

def get_current_weather(lat, lon, api_key):
    if lat == None or lon == None:
        return None
    else:
        weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial').json()
        #weather_data = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}&units=imperial").json()
        #print(weather_data)
        data = WeatherData(
            main = weather_data['weather'][0]['main'],
            description = weather_data['weather'][0]['description'],
            icon = weather_data['weather'][0]['icon'],
            temp = round(weather_data['main']['temp']),
            temp_max = round(weather_data['main']['temp_max']),
            temp_min = round(weather_data['main']['temp_min'])
        )
        return data

def hourly_weather(lat, lon, new_key):
    if lat == None or lon == None:
        return None
    hour_data = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={new_key}&q={lat},{lon}&days=1&aqi=no&alerts=no").json()
    #print(hour_data)
    hourly_data = []
    for hour in hour_data['forecast']['forecastday'][0]['hour']:
        #print(hour)
        date,hr = hour['time'].split()
        time_24hr = datetime.strptime(hr, "%H:%M")
        time_12hr = time_24hr.strftime("%I %p").lstrip('0')
        data = HourlyData(
            time = time_12hr,
            temp = round(hour['temp_f']) ,
            icon = hour['condition']['icon'] ,
            description = hour['condition']['text']
        )
        hourly_data.append(data)
    return hourly_data

def daily_weather(lat, lon, new_key):
    if lat == None or lon == None:
        return None
    day_data = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={new_key}&q={lat},{lon}&days=10&aqi=no&alerts=no").json()
    #print(day_data)
    daily_data = [] 
    for day in day_data['forecast']['forecastday']:
        date_obj = datetime.strptime(day['date'], '%Y-%m-%d')
        formatted_date = date_obj.strftime('%a %d')
        #print(day)
        data = DailyData(
            date = formatted_date,
            description=day['day']['condition']['text'],
            icon=day['day']['condition']['icon'],
            temp_max= round(day['day']['maxtemp_f']),
            temp_min = round(day['day']['mintemp_f']),
            precipitation = (day['day']['daily_chance_of_rain'])
        )
        daily_data.append(data)
    return daily_data

'''def daily_weather(lat, lon, api_key):
    if lat == None or lon == None:
        return None
    day_data = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=imperial").json()
    #print(day_data)
    daily_data = []
    #print(len(day_data['list'])) its 40
    for hour in day_data['list']:
        unx_time = datetime.utcfromtimestamp(hour['dt'])
        data = DailyData(
            time = unx_time.strftime('%a %d %H:%M'),
            description=hour['weather'][0]['description'],
            temp=hour['main']['temp'],
            icon=hour['weather'][0]['icon'],
            temp_max=hour['main']['temp_max'],
            temp_min = hour['main']['temp_min'],
            precipitation = hour['pop']*100
        )
        daily_data.append(data)
    daily_data = daily_data[::8]
    return daily_data'''

def weather_map(api_key):
    map = requests.get(f"https://tile.openweathermap.org/map/clouds/1/1/1.png?appid={api_key}")
    print(map)

def main_current_weather(city_name, state_name, country_name):
    location = True
    lat, lon = get_lat_lon(city_name, state_name, country_name, api_key)
    weather_data = get_current_weather(lat, lon, api_key)
    return weather_data

def main_daily_weather(city_name, state_name, country_name):
    lat, lon = get_lat_lon(city_name, state_name, country_name, api_key)
    weather_data = daily_weather(lat, lon, new_key)
    return weather_data

def main_hourly_weather(city_name, state_name, country_name):
    lat, lon = get_lat_lon(city_name, state_name, country_name, api_key)
    weather_data = hourly_weather(lat, lon, new_key)
    return weather_data

#print(main_hourly_weather('Mission','KS', 'US'))

print(main_daily_weather('Mission','KS', 'US'))
#print(main_current_weather('gra','gre', 'gru'))
#weather_map(api_key)
