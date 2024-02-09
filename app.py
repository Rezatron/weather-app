from flask import Flask, render_template, request, send_from_directory
import requests
from datetime import datetime, timezone
import os 
from utils import get_weather_icon

app = Flask(__name__, static_url_path='/static')

# Fetch weather data function
def fetch_weather_data(city_name):
    api_key = "f5e91c2037fade8e196c8b8b164ab309"  
    url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Specify units for temperature in Celsius
    }
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes

    print(response.json())
    return response.json()

# Process weather data function
def process_weather_data(weather_data):
    processed_data = {}
    for forecast in weather_data['list']:
        date_time = forecast['dt_txt']
        date, time = date_time.split(' ')
        # Convert date string to datetime object
        date = datetime.strptime(date, '%Y-%m-%d')
        temperature = forecast['main']['temp']
        feels_like = forecast['main']['feels_like']
        humidity = forecast['main']['humidity']
        wind_speed = forecast['wind']['speed']
        weather_description = forecast['weather'][0]['description']
        weather_icon_code = forecast['weather'][0]['icon']
        weather_icon = get_weather_icon(weather_icon_code)

        # Group by date
        if date not in processed_data:
            processed_data[date] = []

        processed_data[date].append({
            'time': time,
            'temperature': temperature,
            'feels_like': feels_like,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'weather_description': weather_description,
            'weather_icon': weather_icon,  # Include weather icon path
        })
    return [{'date': key, 'hourly': value} for key, value in processed_data.items()]


@app.route('/forecast', methods=['POST'])
def forecast():
    city_name = request.form['city']
    try:
        weather_data = fetch_weather_data(city_name)
        processed_data = process_weather_data(weather_data)
        
        return render_template('index.html', forecast=processed_data, city=city_name)
    except requests.exceptions.HTTPError as http_err:
        if http_err.response.status_code == 404:
            return render_template('index.html', error=f"Sorry, we couldn't find weather information for {city_name}. Please check the city name and try again.")
        else:
            return render_template('index.html', error=f"Sorry, we encountered an issue while fetching weather data for {city_name}. Error details: {str(http_err)}")
    except requests.exceptions.RequestException as e:
        return render_template('index.html', error="Error fetching weather data. Please try again.")


@app.route('/favicon.ico')
def favicon():
    # Return the favicon.ico file from the static directory
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


# Custom filter for date formatting
@app.template_filter('custom_date_format')
def custom_date_format(date):
    return date.strftime("%A %d")  # Format: Tuesday 8


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)