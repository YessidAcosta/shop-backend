from rest_framework import status, views
from rest_framework.response import Response

from shopApp.serializers.productSerializer import ProductSerializer

class ProductCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        # instantiate the ProductSerializer with the data sent by the request
        serializer = ProductSerializer(data=request.data)
        # validates that the data arrives in the expected format and returns an error otherwise
        serializer.is_valid(raise_exception=True)
        # if the data is correct, call the "create" method to create the product
        serializer.save()
        #product = serializer.save()

        return Response("Product Created",status=status.HTTP_201_CREATED)