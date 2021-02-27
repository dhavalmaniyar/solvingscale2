from django.contrib import admin
from django.urls import path
from . import views
from .views import snippet_detail
from django.views.generic import TemplateView
urlpatterns = [
    path('', views.index, name='index'),
    path('company', views.company, name='company'),
    path('consulting', views.consulting, name='consulting'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('contact', views.contact, name='contact'),
    path('team', views.team, name='team'),
    path("submit", views.submit, name="submit"),
    path('healthcare',views.healthcare,name='healthcare'),
    path('construction',views.construction,name='construction'),
    path('retail',views.retail,name='retail'),
    path('automobile',views.automobile, name='automobile'),
    path('smartcity',views.smartcity,name='smartcity'),
    path('robots.txt',TemplateView.as_view(template_name='robots.txt', content_type="text/plain"),),
    path('<slug:slug>/', snippet_detail),
]
