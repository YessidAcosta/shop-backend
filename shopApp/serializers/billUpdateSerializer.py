from shopApp.models.bill import Bill
from rest_framework import serializers

class BillUpdateSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Bill
        fields = ['bill_date', 'total']

    def validate_bill_date(self, value):
        if(value == ''):
            raise serializers.ValidationError('Error, The bill_date cannot be empty')
        return value
    
    def validate_total(self, value):
        if(value < 0):
            raise serializers.ValidationError('Error, The total must be greater than zero')
        return value
    
    
    def update(self, instance, validated_data):
        instance.bill_date = validated_data.get('bill_date', instance.bill_date)
        instance.total = validated_data.get('total', instance.total)
        instance.save()
        return instance