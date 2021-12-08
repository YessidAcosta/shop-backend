from django.db import models

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    bill_date = models.DateTimeField()
    total  = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.bill_date} {self.total}'