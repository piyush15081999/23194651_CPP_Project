from django.contrib import admin
from .models import Cartitem, Order
# Register your models here.

admin.site.register(Cartitem)
admin.site.register(Order)