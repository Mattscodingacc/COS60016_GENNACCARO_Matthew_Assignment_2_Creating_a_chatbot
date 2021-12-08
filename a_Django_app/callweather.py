from django.shortcuts import render
from requests import request
import json
import requests

# Auth token and API key so I don't forget them.
AUTH_TOKEN = "2da98ec3bb4c75e3e04809e9219aba745d9a935c"
api_key = '8678a0ac32097ae00aac688903ea842d'

# Weather app request.
def weather_call(lat, long):
    data_response = {}
    if lat != '' and long != '':
        # check whether input is alphabetical. If not, error message.
        if lat.isalpha() or long.isalpha() == True:

            # If response contains alphabetical characters, error message.
            data_response = dict(error_message='Alphabetical input detected. '
                                               'Please enter numerical latitude values between -90 and 90, '
                                               'and numerical longitude values between -180 and 180.')

        elif -90.0 <= float(lat) <= 90.0 and -180.0 <= float(long) <= 180.0:

            # API call to obtain weather information for entered latitude and longitude.
            resp = requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}'
                                f'&appid=8678a0ac32097ae00aac688903ea842d&units=metric')

            # Store text of json response in variable.
            json_data = json.loads(resp.text)

            # Build a dictionary of the desired json data to be presented in app.
            data_response = {
                'location': json_data['name'],
                'description': (json_data['weather'][0]['description']).capitalize(),
                'current_temp': str(json_data['main']['temp']) + '°C',
                'min_temp': str(json_data['main']['temp_min']) + '°C',
                'max_temp': str(json_data['main']['temp_max']) + '°C',
                'humidity': str(json_data['main']['humidity']) + '%',
            }
            return data_response

        else:
            # error message in case of invalid input.
            data_response = dict(error_message='Invalid input detected. '
                                                'Please enter latitude values between -90 and 90, '
                                                'and longitude values between -180 and 180.')
    return data_response

# Authentication testing.
'''def authenticate(token):
    if token == AUTH_TOKEN:
        return True
    else:
        return False'''
