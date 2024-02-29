from django.views.generic import ListView, DetailView
from catalogue.models import Locality

#Bilal - Liste des Localites
class ListeLocalitesView(ListView):
    model = Locality
    template_name = "locality/index.html"
    
#Bilal - Detail Localité
class DetailLocaliteView(DetailView):
    model = Locality
    template_name = "locality/show.html"
