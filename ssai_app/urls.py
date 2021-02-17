from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('company', views.company, name='company'),
    path('consulting', views.consulting, name='consulting'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('contact', views.contact, name='contact'),
    path('team', views.team, name='team'),
    path("submit", views.submit, name="submit"),
]
