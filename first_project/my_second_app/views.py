from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    return HttpResponse("some info about us")

def contact(request):
    return HttpResponse("Call this number: 09030556547, or send us an email: winiigboama@gmail.com")
