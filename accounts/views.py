
# Bilal Ma - Auth Accounts 
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
#BM - Formulaire personnalisé - /-->forms
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
from .forms import CustomPasswordResetForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView



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


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
    