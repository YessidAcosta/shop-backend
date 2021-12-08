from rest_framework import serializers
from shopApp.models.sale import Sale
from shopApp.models.product import Product
from shopApp.models.bill import Bill
from shopApp.serializers.billSerializer import BillSerializer
from shopApp.serializers.productSerializer import ProductSerializer

class SaleSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    #bill = BillSerializer()
    class Meta:
        model = Sale
        fields = ['id', 'product', 'bill', 'quantity']

    def create(self, validated_data):
        saleInstance = Sale.objects.create(**validated_data)
        return saleInstance

    def to_representation(self, obj):
        sale = Sale.objects.get(id=obj.id)
        product = Product.objects.get(sale=obj.id)
        bill = Bill.objects.get(sale=obj.id)
        return {
                    'id': sale.id, 
                    # product': sale.product,
                    'product':{
                        'id': product.id,
                        'description': product.description,
                        'price': product.price,
                        'inventory': product.inventory
                    },
                    #'bill': sale.bill,
                    'bill':{
                        'id': bill.id,
                        'bill_date': bill.bill_date,
                        'total': bill.total
                    },
                    'quantity': sale.quantity
                }