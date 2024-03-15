# fichier views.py

from django.shortcuts import render
from catalogue.models import Role, Show

# Bilal Maayoud - Home page catalogue 

def index(request):
    # Récupérer les données des rôles depuis le modèle Role
    roles = Role.objects.all()
    
    # Récupérer les données des spectacles depuis le modèle Show
    shows = Show.objects.all()
    
    # Fournir les données dans le contexte
    context = {'roles': roles, 'shows': shows}
    
    # Rendre le modèle principal en passant le contexte
    return render(request, 'home/index.html', context)
