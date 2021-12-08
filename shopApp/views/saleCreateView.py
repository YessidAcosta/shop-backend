from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from shopApp.serializers.saleSerializer import SaleSerializer

class SaleCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        # instantiate the ProductSerializer with the data sent by the request
        serializer = SaleSerializer(data=request.data)
        # validates that the data arrives in the expected format and returns an error otherwise
        serializer.is_valid(raise_exception=True)
        # if the data is correct, call the "create" method to create the product
        serializer.save()
        #product = serializer.save()

        return Response("Sale Created",status=status.HTTP_201_CREATED)