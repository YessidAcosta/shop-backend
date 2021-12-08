from shopApp.models.user import User
from rest_framework import serializers

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'name', 'email', 'type']

    def validate_username(self, value):
        if(value == ''):
            raise serializers.ValidationError('Error, The username cannot be empty')
        return value

    def validate_password(self, value):
        if(value == ''):
            raise serializers.ValidationError('Error, The password cannot be empty')
        return value
    
    def validate_name(self, value):
        if(value == ''):
            raise serializers.ValidationError('Error, The name cannot be empty')
        return value

    def validate_email(self, value):
        if(value == ''):
            raise serializers.ValidationError('Error, The email cannot be empty')
        return value
    
    def validate_type(self, value):
        if(value == ''):
            raise serializers.ValidationError('Error, The type cannot be empty')
        return value
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.type = validated_data.get('type', instance.type)
        instance.save()
        return instance