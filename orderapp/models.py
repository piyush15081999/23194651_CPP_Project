from django.db import models
from product.models import Prod
from django.contrib.auth.models import User

# Create your models here.
class Cartitem(models.Model):
    prod = models.ForeignKey(Prod, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

# CHOICES = {
#     ("Orderd", "Orderd",),
#     ("Shipped", "Shipped",),
#     ("Deliverd", "Deliverd",),
# }



class Order(models.Model):
    prod = models.ForeignKey(Prod, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    order_main_id = models.CharField(max_length=50)
    status = models.CharField(max_length= 50)