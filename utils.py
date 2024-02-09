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







def get_weather_icon(icon_code):
    icon_mapping = {
        '01d': 'clear_sky_day.png',
        '01n': 'clear_sky_night.png',
        '02d': 'few_clouds_day.png',
        '02n': 'few_clouds_night.png',
        '03d': 'scattered_clouds.png',
        '04d': 'broken_clouds.png',
        '09d': 'shower_rain.png',
        '10d': 'rain_day.png',
        '10n': 'rain_night.png',
        '11d': 'thunderstorm.png',
        '13d': 'snow.png',
        '50d': 'mist.png',
    }

    default_icon = 'no-photos.png'
    icon_filename = icon_mapping.get(icon_code, default_icon)
    


    return f'icons/{icon_filename}'