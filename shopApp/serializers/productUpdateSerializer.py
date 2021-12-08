from shopApp.models.product import Product
from rest_framework import serializers

class ProductUpdateSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Product
        fields = ['description', 'price', 'inventory']

    def validate_description(self, value):
        if(value == ''):
            raise serializers.ValidationError('Error, The description cannot be empty')
        return value
    
    def validate_price(self, value):
        if(value < 0):
            raise serializers.ValidationError('Error, The price must be greater than zero')
        return value
    
    def validate_inventory(self, value):
        if(value < 0):
            raise serializers.ValidationError('Error, The inventory must be greater than zero')
        return value
    
    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.inventory = validated_data.get('inventory', instance.inventory)
        instance.save()
        return instance