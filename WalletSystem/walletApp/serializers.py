from django.db.models.base import Model
from rest_framework import serializers;
from .models import Wallet
class CoreWalletSerializer(serializers.ModelSerializer):
    """
    for create and activate wallet
    """
    class Meta:
        model=Wallet;
        fields=["phone","password","balance"]
        read_only_fields = ["balance"]
class WalletOperationSerializer(serializers.ModelSerializer):
    """
    for debit and credit wallet
    """
    amount=serializers.FloatField(source="balance")
    class Meta:
       model=Wallet;
       fields=["phone","password","amount"]