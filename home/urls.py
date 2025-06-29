from django.urls import path
from .views import ContactUsView

app_name = 'home'
urlpatterns = [
    path('',ContactUsView.as_view(),name='contact-us'),
]