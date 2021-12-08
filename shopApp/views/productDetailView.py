from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend

from shopApp.models.product import Product
from shopApp.serializers.productSerializer import ProductSerializer
from shopApp.serializers.productUpdateSerializer import ProductUpdateSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        print("Request:", self.request)
        print("Args:", self.args)
        print("KWArgs:", self.kwargs)

        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        product = Product.objects.filter(id=kwargs['pk']).first()
        product_serializer = ProductUpdateSerializer(product, data=request.data)

        if (product):
            if (product_serializer.is_valid()):
                product_serializer.save()
                return Response({'message': 'updated product'} , status=status.HTTP_200_OK)
            else:
                return Response(product_serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'product not found'} , status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        product = Product.objects.filter(id=kwargs['pk']).first()
        
        if (product):
            product.delete()
            return Response({'message': 'product removed'} , status=status.HTTP_200_OK)
        return Response({'message': 'product not found'} , status=status.HTTP_404_NOT_FOUND)