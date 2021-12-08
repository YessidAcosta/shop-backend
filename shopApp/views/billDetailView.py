from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend

from shopApp.models.bill import Bill
from shopApp.serializers.billSerializer import BillSerializer
from shopApp.serializers.billUpdateSerializer import BillUpdateSerializer

class BillListView(generics.ListAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class BillDetailView(generics.RetrieveAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    def get(self, request, *args, **kwargs):
        print("Request:", self.request)
        print("Args:", self.args)
        print("KWArgs:", self.kwargs)

        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        bill = Bill.objects.filter(id=kwargs['pk']).first()
        bill_serializer = BillUpdateSerializer(bill, data=request.data)

        if (bill):
            if (bill_serializer.is_valid()):
                bill_serializer.save()
                return Response({'message': 'updated bill'} , status=status.HTTP_200_OK)
            else:
                return Response(bill_serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'bill not found'} , status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        bill = Bill.objects.filter(id=kwargs['pk']).first()
        
        if (bill):
            bill.delete()
            return Response({'message': 'bill removed'} , status=status.HTTP_200_OK)
        return Response({'message': 'bill not found'} , status=status.HTTP_404_NOT_FOUND)