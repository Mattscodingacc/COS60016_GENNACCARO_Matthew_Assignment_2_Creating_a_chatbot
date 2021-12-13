from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm, WeatherForm
import json
from .callweather import weather_call

# Views for different requests.

# Home page, only displaying text.
def home(request):
    return render(request, 'home.html')

# About us page, only displaying text.
def about_us(request):
    return render(request, 'about_us.html')

# FAQ page, only contains text.
def frequently_asked_questions(request):
    return render(request, 'FAQ.html')

# Future page to simply display a "coming soon" message.
def the_future(request):
    return render(request, 'the_future.html')

# Customer feedback page, contains a form for feedback submission. Not currently functional to store submitted data.
def customer_feedback(request):
    # if this is a POST request we need to process the form data.
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            # print data to terminal.
            print("Name: " + name, "E-mail: " + email, "Phone number: " + phone_number, "Address: " + address)
            # redirect to new URL (could be a "thanks for submission" page in future), left as feedback html for now.
            return HttpResponseRedirect('/customer_feedback')
    # if a GET (or other method) we'll create a blank form.
    else:
        form = ContactForm()
    return render(request, 'customer_feedback.html', {'form': form})

# Weather app request to use weather_call function to query API and return response.
def weather_app(request):
    data_response = {}
    # is this is a POST request we need to process the data.
    if request.method == 'POST':

        # assign input of latitude and longitude to variables.
        lat = request.POST['latitude']
        long = request.POST['longitude']
        if lat != '' and long != '':

            # Pass latitude and longitude to weather call function that makes api call and returns dictionary.
            data_response = weather_call(lat, long)

    return render(request, 'weather_app.html', data_response)

