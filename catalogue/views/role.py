from django.views.generic import ListView, DetailView
from catalogue.models import Role

class RoleListView(ListView):
    model = Role
    template_name = "role/index.html"
    paginate_by = 10  

class RoleDetailView(DetailView):
    model = Role
    template_name = "role/index.html"