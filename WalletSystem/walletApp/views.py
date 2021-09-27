from django.http import response
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response;
from rest_framework.decorators import action, authentication_classes;
from rest_framework import status
from rest_framework.serializers import Serializer;
from django.contrib.auth.hashers import make_password;
from .models import Wallet;
from .serializers import *;
from .decorators import *;
import sys;
class WalletViewset(viewsets.ModelViewSet):
    """
    include wallet operation like create , activate , credit and debit
    """
    serializer_class=CoreWalletSerializer;
    @action(methods=["POST"],detail=True)
    @checkWalletExistance(False)
    @checkPhoneNumberFormat
    @checkWalletPasswordFormat
    def create_wallet(self,request):
        """
        responsible for creating wallet
        """
        
        try:
            create_serializer=self.get_serializer_class();
            serializer=create_serializer(data=request.data)
            serializer.is_valid(raise_exception=True);
            password=serializer.validated_data.get("password");
            print("parsed password is:",password);
            serializer.save(password=make_password(password));

            return Response({"phone":serializer.data.get("phone"),"balance":serializer.data.get("balance")},status=status.HTTP_201_CREATED);
        except ValidationError as E:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as E:
            print(sys.exc_info())
            raise InternalServerError;
    
