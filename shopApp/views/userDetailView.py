from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from shopApp.models.user import User
from shopApp.serializers.userSerializer import UserSerializer
from shopApp.serializers.userUpdateSerializer import UserUpdateSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
    
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        return super().get(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        user = User.objects.filter(id=kwargs['pk']).first()
        user_serializer = UserUpdateSerializer(user, data=request.data)

        if (user):
            if (user_serializer.is_valid()):
                user_serializer.save()
                return Response({'message': 'updated user'} , status=status.HTTP_200_OK)
            else:
                return Response(user_serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'user not found'} , status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        user = User.objects.filter(id=kwargs['pk']).first()
        
        if (user):
            user.delete()
            return Response({'message': 'user removed'} , status=status.HTTP_200_OK)
        return Response({'message': 'user not found'} , status=status.HTTP_404_NOT_FOUND)