from shopApp.models.product import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['description', 'price', 'inventory']
    
    def create(self, validated_data):
        # create a user with the information required by the files variable and this is associated with the productInstance variable
        productInstance = Product.objects.create(**validated_data)
        # returns the variable userInstance
        return productInstance
        
    def to_representation(self, obj):
        product = Product.objects.get(id=obj.id)       
        return {
                    'id'                : product.id,
                    'description'       : product.description,
                    'price'             : product.price,
                    'inventory'         : product.inventory
                }