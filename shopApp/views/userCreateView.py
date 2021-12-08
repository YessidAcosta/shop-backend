from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from shopApp.serializers.userSerializer import UserSerializer

class UserCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        # instantiate the UserSerializer with the data sent by the request
        serializer = UserSerializer(data=request.data)
        # validates that the data arrives in the expected format and returns an error otherwise
        serializer.is_valid(raise_exception=True)
        # if the data is correct, call the "create" method to create the user 
        serializer.save()

        # generate an object to log in
        tokenData = {"username":request.data["username"], 
                     "password":request.data["password"]}
        # send the credentials through the TokenObtainPairSerializer to obtain the refresh and access token
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        # validates that the data arrives in the expected format and returns an error otherwise
        tokenSerializer.is_valid(raise_exception=True)
        # returns the valid information in the serializer
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)