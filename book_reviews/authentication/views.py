from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

# Create your views here.
def sign_up(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success("Account created successfully")
            return redirect("authentication:log_in")
    context = {"form": form}
    return render(request, "authentication/sign-up.html", context)