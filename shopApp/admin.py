from django.contrib import admin
from .models.user import User
from .models.product import Product
from .models.bill import Bill
from .models.sale import Sale

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Bill)
admin.site.register(Sale)
