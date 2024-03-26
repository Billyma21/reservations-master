#Bilal Ma - Urls Accounts 

from django.urls import path
from . import views
from .views import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView

app_name = "accounts"

urlpatterns = [
    path ('login/', views.login_user, name = 'login'),
    path ('logout/', views.logout_user, name = 'logout'),
    path ('register/', views.register_user, name = 'register'),
    path('registration-success/', views.registration_success, name='registration_success'), 
   #Bilal ma - reset password : 
    path('password-reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    #Bilal ma - Change mots de passe ou pseudo, quand utilisateur est Co : 
    path('password-change/', views.change_password, name='change_password'),
    path('change-username/', views.change_username, name='change_username'),


]

