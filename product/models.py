from django.db import models

# Create your models here.

class Category(models.Model):
    cat_name= models.CharField(max_length= 50)

class Subcategory(models.Model):
    subcat_name= models.CharField(max_length= 50)    
    cat= models.ForeignKey(Category, on_delete=models.PROTECT)

class Prod(models.Model):
    prod_name= models.CharField(max_length= 50)
    subcat= models.ForeignKey(Subcategory, on_delete=models.PROTECT)
    prod_image = models.ImageField(upload_to='images')
    prod_desc= models.TextField()
    prod_price= models.FloatField(null=True, blank=True, default=None)
