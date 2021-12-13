from django.shortcuts import render
from .chatbot_logic import talk, qa_data
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import ChatBotForm
import json
import requests
from datetime import datetime

# API key for calls.
api_key = '8678a0ac32097ae00aac688903ea842d'


# Create your views here.

# View for chatbot.
@method_decorator(csrf_exempt, name='dispatch')
def chatbot(request):
    question = ''
    answer = ''
    # if this is a POST request we need to process the form data.
    if request.method == 'POST':
        # create a form instance and populate it with data from the request.
        form = ChatBotForm(request.POST)
        # check whether it's valid.
        if form.is_valid():
            # if valid, process the data in form.cleaned_data as required.
            question = form.cleaned_data['question']
            question_words = question.strip("?").split()
            # print data to terminal. Useful for observing the obtained data.
            print("question: " + question)
            # if the question asked is present in the QnA json file, use appropriate answer.
            if question in qa_data:
                answer = talk(question)
                form = ChatBotForm()
                return render(request, 'chatbot.html',
                              {'user_input_form': form, 'question': question, 'answer': answer})

            # take last word of input as city name. Store in variable to use in API call.
            cityname = question_words[-1]
            # API call to obtain weather information for entered location.
            resp = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={api_key}'
                                f'&units=metric')
            # Store text of json response in variable. Pull desired data from json data and store in variables.
            json_data = json.loads(resp.text)

            # If "temperature" is in the question, call API for temperature of the city.
            if "temperature" in question_words:
                print(json_data)
                temp_data = json_data['main']['temp']
                feels_like = str(json_data['main']['feels_like'])
                # store response from chatbot in answer variable, to be returned to the page.
                answer = "The current temperature in " + cityname + " is " + str(temp_data) + "°C. It feels like " \
                         + feels_like + "°C."

            # If "humidity" is in the question, call API for humidity of the city.
            elif "humidity" in question_words:
                print(json_data)
                humidity_data = json_data['main']['humidity']
                # store response from chatbot in answer variable, to be returned to the page.
                answer = "The humidity in " + cityname + " is " + str(humidity_data) + "%."

            # If "weather", "located in" or "I'm in" are in the question, call API for weather description.
            elif ("weather" in question_words) or ("located in" in question) or ("I'm in" in question):
                print(json_data)
                weather_description = str(json_data['weather'][0]['description'])
                # store response from chatbot in answer variable, to be returned to the page.
                answer = "The current weather in " + cityname + " is " + weather_description + "."

            # if "sunrise" is in the question, use datetime module and API call to get correct sunrise time of location.
            # Some locations do not show correct time at present.
            elif "sunrise" in question_words:
                print(json_data)
                sunrise = datetime.utcfromtimestamp(json_data['sys']['sunrise']).strftime('%H:%M')
                # store response from chatbot in answer variable, to be returned to the page.
                answer = "Sunrise in " + cityname + " is at " + sunrise + "."

            # if "sunset" is in the question, use datetime module and API call to get correct sunset time of location.
            # Some locations do not show correct time at present.
            elif "sunset" in question_words:
                print(json_data)
                sunset = datetime.utcfromtimestamp(json_data['sys']['sunset']).strftime('%H:%M')
                # store response from chatbot in answer variable, to be returned to the page.
                answer = "Sunset in " + cityname + " is at " + sunset + "."

            # if no conditions are met, display an error message.
            else:
                answer = "I'm sorry, I don't understand your question. Please ask another."
    # return form to blank state.
    form = ChatBotForm()
    # render the page and include relevant data.
    return render(request,  'chatbot.html', {'user_input_form': form, 'question': question, 'answer': answer})
