#je n'y arrive pas
'''
from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Show


class LatestEntriesFeed(Feed):
    title = "Derniers Spectacles"
    link = "/lastshow/"
    description = "Check out our new shows."

    def items(self):
        return Show.objects.order_by("updated_at")[:5]

    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return item.description
    
    #besoin que le frontend soit pret pour inserer le lien.
    def item_link(self, item):
        return reverse("show_show", args=[item.pk])
'''