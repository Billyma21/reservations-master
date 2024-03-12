# catalogue/views/role.py

from django.shortcuts import render
from django.http import Http404
from catalogue.models import Role

def index(request):
    roles = Role.objects.all()
    title = 'Liste des rôles'
    
    return render(request, 'role/index.html', {
        'roles': roles,
        'title': title,
    })

def show(request, role_id):
    try:
        role = Role.objects.get(id=role_id)
    except Role.DoesNotExist:
        raise Http404('Rôle inexistant')
    
    title = "Fiche d'un rôle"
    
    return render(request, 'role/show.html', {
        'role': role,
        'title': title,
    })
