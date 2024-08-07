# core/urls.py
from django.urls import path
from .views import home, contact, store, about

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('store/', store, name='store'),
    path('about/', about, name='about'),
]
