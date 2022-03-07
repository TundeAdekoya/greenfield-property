from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name='home'),
    path('buy/', views.buy, name='buy'),
    path('rent/', views.rent, name='rent'),
]
