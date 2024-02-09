from datetime import datetime


def display_weather_info(user_input, temperature_celsius, description, sunrise_formatted, sunset_formatted, weather_icon):
    current_date = datetime.now()

    if current_date:
        print(f'Date: {current_date.strftime("%Y-%m-%d %H:%M:%S")}')
    print(f'Temperature in {user_input}: {temperature_celsius:.2f} Celsius')
    print(f'Weather description: {description}')

    print(f'Weather icon path: {weather_icon}')

    return {
        'date': current_date.strftime('%Y-%m-%d %H:%M:%S'),
        'temperature_celsius': temperature_celsius,
        'description': description,

        'weather_icon': weather_icon,
    }

