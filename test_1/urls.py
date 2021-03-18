from django.urls import path
from . import views
from contact_form.views import ContactForm
from .views import ContactCreate, success    
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.index, name = 'index'),
    
]