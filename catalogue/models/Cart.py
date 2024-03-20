from django.db import models
from catalogue.models import Show

class Cart(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} {self.show.title}(s) in your cart"

    def total_price(self):
        return self.quantity * self.show.price