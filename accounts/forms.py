# Bilal Maayoud - accounts/forms.py 

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext as _

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=150, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.')
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(), help_text='Your password can’t be too similar to your other personal information. Your password must contain at least 8 characters. Your password can’t be a commonly used password. Your password can’t be entirely numeric.')
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(), help_text='Enter the same password as before, for verification.')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('username', 'first_name', 'last_name', 'email')


class CustomPasswordResetForm(PasswordResetForm):
    pass 


#Billy ma - Pour changer mots_passe et pseudo quand utilisateur est co
#POUR-->mots_passe
class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Ancien mot de passe"), widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _("Ancien mot de passe")}))
    new_password1 = forms.CharField(label=_("Nouveau mot de passe"), widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _("Nouveau mot de passe")}))
    new_password2 = forms.CharField(label=_("Confirmer le nouveau mot de passe"), widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _("Confirmer le nouveau mot de passe")}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
#POUR-->pseudo
class ChangeUsernameForm(forms.Form):
    new_username = forms.CharField(label='Nouveau pseudo', max_length=150)

    def clean_new_username(self):
        new_username = self.cleaned_data['new_username']
        if User.objects.filter(username=new_username).exists():
            raise forms.ValidationError("Ce pseudo est déjà pris. Veuillez en choisir un autre.")
        return new_username