from flask import Flask, render_template, request, send_from_directory
import requests
from datetime import datetime, timezone
import os 

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
    return response.json()

# Process weather data function
def process_weather_data(weather_data):
    processed_data = []
    city_name = weather_data['city']['name']
    city_sunrise = weather_data['city']['sunrise']
    city_sunset = weather_data['city']['sunset']

    for forecast in weather_data['list']:
        date_time = forecast['dt_txt']
        temperature = forecast['main']['temp']
        feels_like = forecast['main']['feels_like']
        humidity = forecast['main']['humidity']
        wind_speed = forecast['wind']['speed']
        weather_description = forecast['weather'][0]['description']

        processed_data.append({
            'date_time': date_time,
            'temperature': temperature,
            'feels_like': feels_like,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'weather_description': weather_description,
        })
    return processed_data



print(process_weather_data)



@app.route('/')
def index():
    return render_template('index.html')

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

if __name__ == "__main__":
    app.run(debug=True)