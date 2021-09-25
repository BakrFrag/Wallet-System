from rest_framework import viewsets
from rest_framework.response import Response;
from rest_framework.decorators import action, authentication_classes;
from rest_framework import status
from rest_framework.serializers import Serializer
from .models import Wallet;
from .serializers import *;

class WalletViewset(viewsets):
    """
    include wallet operation like create , activate , credit and debit
    """
    @action(methods=["POST"],detail=True)
    def create_wallet(self,request,*args,**kwargs):
        """
        responsible for creating wallet
        """
        try:
            serializer=CoreWalletSerializer(request.data);
            serializer.is_valid(raise_exception=True);
            serializer.save();
            return Response({"phone":serializer.phone,"balance":serializer.balance},status=status.HTTP_201_CREATED);
            
        except Exception as E:
            return Response({"message":"internal server error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
