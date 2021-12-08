from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField('Description', max_length = 50)
    price = models.IntegerField(default=0)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.description} {self.price} {self.inventory}'