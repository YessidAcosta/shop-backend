from rest_framework import serializers
from shopApp.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email', 'type']

    def create(self, validated_data):
        # create a user with the information required by the files variable and this is associated with the userInstance variable
        userInstance = User.objects.create(**validated_data)
        # returns the variable userInstance
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)     
        return {
                    'id':       user.id, 
                    'username': user.username,
                    'name':     user.name,
                    'email':    user.email,
                    'type':     user.type
                }