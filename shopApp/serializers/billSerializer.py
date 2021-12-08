from shopApp.models.bill import Bill
from shopApp.models.sale import Sale
from shopApp.models.product import Product
from rest_framework import serializers

#from shopApp.serializers.saleSerializer import SaleSerializer

class BillSerializer(serializers.ModelSerializer):
    #sale = SaleSerializer()
    class Meta:
        model = Bill
        #fields = ['bill_date', 'total', 'sale']
        fields = ['bill_date', 'total']
        
    def create(self, validated_data):
        #saleData = validated_data.pop('sale')
        billInstance = Bill.objects.create(**validated_data)
        #Sale.objects.create(bill=billInstance, **saleData)
        return billInstance
        
    def to_representation(self, obj):
        bill = Bill.objects.get(id=obj.id)
        #sale = Sale.objects.get(bill=obj.id)
        #product = Product.objects.get(sale=obj.id)    
        return {
                    'id'                : bill.id,
                    'bill_date'         : bill.bill_date,
                    'total'             : bill.total
                    #'sale': {
                    #        'product': sale.id,
                    #        'quantity': sale.id,
                    #}
                    #'sale': {
                    #            'id'    : sale.id,
                    #            'produc': {
                    #                       'id': product.id,
                    #                       'description': product.description,
                    #                       'price': product.price,
                    #                       'inventory': product.inventory
                    #            },
                    #            'quantity': sale.product
                    #}
                }
