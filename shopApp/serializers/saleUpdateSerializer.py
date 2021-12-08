from shopApp.models.sale import Sale
from rest_framework import serializers

class SaleUpdateSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Sale
        fields = ['product', 'bill', 'quantity']

    def validate_product(self, value):
        if(value == ''):
            raise serializers.ValidationError('Error, The product cannot be empty')
        return value
    
    def validate_bill(self, value):
        if(value == ''):
            raise serializers.ValidationError('Error, The bill cannot be empty')
        return value
    
    def validate_quantity(self, value):
        if(value == ''):
            raise serializers.ValidationError('Error, The quantity cannot be empty')
        return value
    
    def update(self, instance, validated_data):
        instance.product = validated_data.get('product', instance.product_id)
        instance.bill = validated_data.get('bill', instance.bill_id)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance