from .models import Wallet;
from django.core.exceptions import ObjectDoesNotExist
def getWallet(phone_number):
    """
    helper function check if wallet with phone number exists or not
    """
    try:
        walletobj=Wallet.objects.get(phone=phone_number);
        return {"exists":True,"wallet":walletobj}
    except Wallet.DoesNotExist as E:
        return {"exists":False,"wallet":None};