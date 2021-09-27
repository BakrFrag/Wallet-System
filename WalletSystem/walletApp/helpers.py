from .models import Wallet;
from django.core.exceptions import ObjectDoesNotExist
def getWallet(phone_number):
    """
    helper function check if wallet with phone number exists or not
    """
    try:
        Wallet.objects.get(phone=phone_number);
        return True;
    except Wallet.DoesNotExist as E:
        return False;