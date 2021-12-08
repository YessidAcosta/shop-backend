from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from shopApp.serializers.billSerializer import BillSerializer

class BillCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        print("Request:", self.request)
        print("Args:", self.args)
        print("KWArgs:", self.kwargs)
        # instantiate the UserSerializer with the data sent by the request
        serializer = BillSerializer(data=request.data)
        # validates that the data arrives in the expected format and returns an error otherwise
        serializer.is_valid(raise_exception=True)
        # if the data is correct, call the "create" method to create the user 
        serializer.save()

        return Response('Bill Created', status=status.HTTP_201_CREATED)