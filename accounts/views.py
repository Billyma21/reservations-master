from django.shortcuts import render, redirect

# Bilal Ma - Auth Accounts 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
#BM - Formulaire personnalisé - /-->forms
from .forms import UserRegistrationForm
from django.urls import reverse_lazy



def login_user(request):
    if request.method == "POST":  
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("catalogue:home_index")  
        else:
            messages.info(request, "Identifiant ou mot de passe incorrects")
            form = AuthenticationForm()
            return render(request, "accounts/login.html", {"form": form})  
    else:
        form = AuthenticationForm()
        return render(request, "accounts/login.html", {"form": form})
    
    

def logout_user(request):
    logout(request)
    return redirect("/")

def registration_success(request):
    return render(request, 'accounts/registration_success.html') 

def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('accounts:registration_success'))  # reverse_lazy() pour obtenir l'URL associée au nom de l'URL 'registration_success'
    else:
        form = UserRegistrationForm()  
    return render(request, "accounts/register.html", {"form": form})
