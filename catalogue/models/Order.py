# Bilal Ma - models/Order.py
from django.db import models
from django.contrib.auth.models import User
from catalogue.models import Show 

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100)
    payment_confirmed = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    # Champ pour stocker les identifiants des spectacles commandés et les quantités
    ordered_items = models.ManyToManyField(Show, through='OrderItem')

    def __str__(self):
        return f"Order #{self.id} - User: {self.user.username}, Total Amount: {self.total_amount}, Payment Method: {self.payment_method}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"OrderItem - Order: {self.order.id}, Show: {self.show.title}, Quantity: {self.quantity}"