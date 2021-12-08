from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend

from shopApp.models.sale import Sale
from shopApp.serializers.saleSerializer import SaleSerializer
from shopApp.serializers.saleUpdateSerializer import SaleUpdateSerializer

class SaleListView(generics.ListAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    
    def get(self, request, *args, **kwargs):
        print("Request:", self.request)
        print("Args:", self.args)
        print("KWArgs:", self.kwargs)
        return super().get(request, *args, **kwargs)

class SaleDetailView(generics.RetrieveAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    def get(self, request, *args, **kwargs):
        print("Request:", self.request)
        print("Args:", self.args)
        print("KWArgs:", self.kwargs)

        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        sale = Sale.objects.filter(id=kwargs['pk']).first()
        sale_serializer = SaleUpdateSerializer(sale, data=request.data)

        if (sale):
            if (sale_serializer.is_valid()):
                sale_serializer.save()
                return Response({'message': 'updated sale'} , status=status.HTTP_200_OK)
            else:
                return Response(sale_serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'sale not found'} , status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        sale = Sale.objects.filter(id=kwargs['pk']).first()
        
        if (sale):
            sale.delete()
            return Response({'message': 'sale removed'} , status=status.HTTP_200_OK)
        return Response({'message': 'sale not found'} , status=status.HTTP_404_NOT_FOUND)