from django.contrib import admin
from .models import Category, Subcategory, Prod
# Register your models here.
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Prod)