from django.urls import path
from . import views

# Dictionary of paths for web pages and respective views.
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('frequently_asked_questions', views.frequently_asked_questions, name='FAQ'),
    path('customer_feedback', views.customer_feedback, name='customer_feedback'),
    path('the_future', views.the_future, name='the_future'),
    path('about_us', views.about_us, name='about_us'),
    path('weather_app', views.weather_app, name='weather_app'),
]
