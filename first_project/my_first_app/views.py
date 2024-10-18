from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Hello. This is my first Django view.")

def introduction(request):
    return HttpResponse("My name is Winnie")