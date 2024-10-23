from django.shortcuts import render

# Create your views here.
def clothes(request):
    return render(request, 'clothes/clothes.html')

