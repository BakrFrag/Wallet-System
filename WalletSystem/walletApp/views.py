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
    
    @action(methods=["POST"],detail=True)
    @checkWalletExistance(True)
    @checkPhoneNumberFormat
    @checkWalletPasswordFormat
    @checkWalletPassword
    @checkWalletActivation(False)
    def activateWallet(self,request):
        """
        viewsets function to activate wallet
        """
        try:
            print("parsed request data:",request.data)
            serializer=CoreWalletSerializer(data=request.data);
            serializer.is_valid(raise_exception=True);
            instance=getWallet(serializer.data.get("phone")).get("wallet")
            serializer.update(instance=instance,validated_data={"is_active":True});
            return Response({"phone":instance.phone,"balance":instance.balance,"is_ctive":instance.is_active},status=status.HTTP_200_OK);
        except ValidationError as E:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as E:
            print(sys.exc_info())
            raise InternalServerError;
    @action(methods=["GET"],detail=True)
    @checkWalletExistance(True)
    @checkWalletPassword
    @checkWalletActivation(True)
    def getWalletInfo(self,request):
        """
        get wallet properties
        """
        try:
             required_field=request.GET.get("q");
             serializer=CoreWalletSerializer(data=request.data);
             serializer.is_valid(raise_exception=True);
             instance=getWallet(serializer.data.get("phone")).get("wallet");
             if hasattr(instance,required_field):
                 return Response({"phone":instance.phone,required_field:getattr(instance,required_field)},status=status.HTTP_200_OK);
             raise UnknownPropertyError
             
        except ValidationError as E:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as E:
            print(sys.exc_info())
            raise InternalServerError;

    @action(methods=["PUT"],detail=True)
    @checkWalletExistance(True)
    @checkPhoneNumberFormat
    @checkWalletPasswordFormat
    @checkWalletPassword
    @checkWalletActivation(True)
    def creditWalletBalance(self,request):
        """
        to credit wallet balance 
        """
        try:
            serializer=WalletOperationSerializer(data=request.data);
            serializer.is_valid(raise_exception=True);
            amount=serializer.validated_data.get("amount")
            if amount <=0:
                raise CreditWalletException;
            phone=serializer.validated_data.get("phone");
            instance=getWallet(phone);
            serializer.update({
                "balance":instance.balance + amount },instance=instance);
            return Response({"phone":phone,"balance":serializer.data.get("balance")},status=status.HTTP_200_OK)
        except ValidationError as E:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as E:
            print(sys.exc_info())
            raise InternalServerError;
    

    @action(methods=["PUT"],detail=True)
    @checkWalletExistance(True)
    @checkPhoneNumberFormat
    @checkWalletPasswordFormat
    @checkWalletPassword
    @checkWalletActivation(True)
    def debitWalletBalance(self,request):
        """
        to debit wallet balance 
        """
        try:
            serializer=WalletOperationSerializer(data=request.data);
            serializer.is_valid(raise_exception=True);
            instance=getWallet(phone).wallet
            amount=serializer.validated_data.get("amount")
            if amount > instance.balace :
                raise DebitWalletException;
            phone=serializer.validated_data.get("phone");
            
            serializer.update({
                "balance":instance.balance - amount },instance=instance);
            return Response({"phone":phone,"balance":serializer.data.get("balance")},status=status.HTTP_200_OK)
        except ValidationError as E:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as E:
            print(sys.exc_info())
            raise InternalServerError;
    

            
