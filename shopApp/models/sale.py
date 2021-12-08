from django.db import models
from .product import Product
from .bill import Bill

class Sale(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, related_name='sale', on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill, related_name='sale', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.product_id} {self.bill_id} {self.quantity}'