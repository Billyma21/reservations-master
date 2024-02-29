from django.views.generic import ListView, DetailView
from catalogue.models import Locality

class ListeLocalitesView(ListView):
    model = Locality
    template_name = "locality/index.html"

class DetailLocaliteView(DetailView):
    model = Locality
    template_name = "locality/show.html"
