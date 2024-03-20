# Dans le fichier views.py

from django.shortcuts import render
from django import forms
from catalogue.models import Role, Show

def index(request):
    roles = Role.objects.all()
    shows = Show.objects.all()

    # BM- Barre de recherche de filtre directement dans la vue
    class ShowFilterForm(forms.Form):
        search = forms.CharField(label='Recherche', max_length=100, required=False)

    # Traitement du formulaire de filtre
    if request.method == 'GET':
        form = ShowFilterForm(request.GET)
        if form.is_valid():
            search = form.cleaned_data.get('search')
            if search:
                shows = shows.filter(title__icontains=search)
    else:
        form = ShowFilterForm()

    context = {'roles': roles, 'shows': shows, 'form': form}
    return render(request, 'home/index.html', context)
