from django.db import models
from django.core.validators import MinValueValidator
from groceries.models import Customers,Products

# Create your models here.
# Cart Model
class Cart(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    total = models.FloatField(default=0.00, validators=[MinValueValidator(0, "total can't be smaller than zero")])

    def __str__(self):
        if self.completed:
            return "Cart{0} with total {1} is completed".format(self.cart_id, self.total)
        else:
            return "Cart{0} with total {1} is not completed".format(self.cart_id, self.total)


class Cart_items(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return "Cart{0} has {1} product{2}".format(self.cart, self.quantity. self.product)