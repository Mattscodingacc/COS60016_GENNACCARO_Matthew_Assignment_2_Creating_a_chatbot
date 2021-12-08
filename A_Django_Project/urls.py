from django.contrib import admin
from django.urls import path, include

# Create dictionary of paths for pages on website.
urlpatterns = [
    path('', include('a_Django_app.urls')),
    #path('home', include('a_Django_app.urls')),
    path('admin/', admin.site.urls),
    #path('FAQ', include('a_Django_app.urls')),
    #path('customer_feedback', include('a_Django_app.urls')),
    #path('our_future', include('a_Django_app.urls')),
    #path('about_us', include('a_Django_app.urls')),
    path('weather_app/', include('a_Django_app.urls')),
    path('chatbot/', include('chatbot.urls')),
    ]
