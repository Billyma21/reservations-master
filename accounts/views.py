
# Bilal Ma - Auth Accounts 
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
#BM - Formulaire personnalisé - /-->forms
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
from .forms import CustomPasswordResetForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
#BM - Changer, depuis le compte, le mt_passe & pseudo
from .forms import ChangeUsernameForm
from django.http import JsonResponse
from django.contrib.auth.models import User



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
    
    
from django.contrib.auth import update_session_auth_hash

# Billy-ma pour changer le mot de passe, lorsqu'on est co
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Met à jour la session d'authentification
            messages.success(request, 'Votre mot de passe a été changé avec succès.')
            return redirect('profil')  # Redirige vers la page de profil ou toute autre page après le changement de mot de passe
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

# Billy-ma pour changer le pseudo, lorsqu'on est co

def change_username(request):
    if request.method == 'POST':
        form = ChangeUsernameForm(request.POST)
        if form.is_valid():
            new_username = form.cleaned_data['new_username']
            request.user.username = new_username
            request.user.save()
            messages.success(request, 'Votre pseudo a été modifié avec succès !')
            return redirect('catalogue:home_index')
    else:
        form = ChangeUsernameForm()
    return render(request, 'change_username.html', {'form': form})

# Billy-ma pour Verifier que pseudo existe ou pas 
def check_username_availability(request):
    username = request.GET.get('username', None)
    if username is not None:
        if User.objects.filter(username=username).exists():
            # Le pseudo est déjà pris
            return JsonResponse({'available': False})
        else:
            # Le pseudo est disponible
            return JsonResponse({'available': True})
    else:
        # Aucun pseudo fourni dans la requête
        return JsonResponse({'error': 'Aucun pseudo fourni dans la requête'}, status=400)