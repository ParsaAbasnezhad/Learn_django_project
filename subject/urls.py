from django.urls import path
from .import views

urlpatterns = [
    path('jee/', views.jee, name='jee'),
]