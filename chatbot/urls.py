from django.urls import path
from . import views


app_name = 'chatbot'

# Dictionary of paths for web pages and respective views.
urlpatterns = [
    # path('', views.chatbot),
    path('chatbot/', views.chatbot)
]
