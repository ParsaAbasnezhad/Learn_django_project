from django.urls import path
from .views import ContactUsView
from . import views

app_name = 'home'
urlpatterns = [

    path('', ContactUsView.as_view(), name='contact-us'),
]
