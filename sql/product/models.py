from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  # Product name
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Product price
    description = models.TextField()  # Product description
    stock = models.IntegerField()  # Quantity available in stock
    category = models.CharField(max_length=50)  # Product category
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for last update

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name
