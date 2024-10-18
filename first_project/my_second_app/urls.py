from django.urls import path

from . import views

urlpatterns = [
    path('about-us/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]