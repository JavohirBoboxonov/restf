from django.db import models

# Create your models here

class Product(models.Model):
    brand = models.CharField(max_length=20)
    title = models.CharField(max_length=40)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    
    
    def __str__(self):
        return self.title