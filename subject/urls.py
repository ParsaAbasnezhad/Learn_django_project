from django.urls import path
from .import views

app_name = 'subject'
urlpatterns = [
    path('jee/', views.jee, name='jee'),
]