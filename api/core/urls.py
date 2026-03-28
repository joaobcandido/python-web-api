from django.urls import path
from . import views

urlpatterns = [
    path('', views.health, name='health'),
    path('ping/', views.ping, name='ping'),
    path('hello/', views.hello, name='hello'),
]
