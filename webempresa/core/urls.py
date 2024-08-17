# core/urls.py
from django.urls import path
from .views import home, store, about

urlpatterns = [
    path('', home, name='home'),
    path('store/', store, name='store'),
    path('about/', about, name='about'),
]
