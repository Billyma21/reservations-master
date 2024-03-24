"""
from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import *


class LatestEntriesFeed(Feed):
    title = "Latest Shows"
    link = "/show/"
    description = "Check out our new shows."

    def items(self):
        return Show.objects.order_by("updated_at")[:5]

    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return item.description
    
    #problème, aucune idée pourquoi.
    def item_link(self, item):
        return reverse("news-item", args=[item.pk])
"""