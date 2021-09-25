import re;
from functools import wraps
from wallet.exceptions import WalletExist;
from django.core.exceptions import ObjectDoesNotExist
from .models import Wallet;
from .exceptions import *;
phone_number_pattern=re.compile(r"(\+2)?([0-9]{11})$")
wallet_password_pattern=re.compile(r"([0-9]{6})$");
def getWallet(phone_number):
    """
    helper function check if wallet with phone number exists or not
    """
    try:
        Wallet.objects.get(phone=phone_number);
        return True;
    except ObjectDoesNotExist:
        return False;
def checkWalletExistance(exist):
        """
        check wallet exists or not according to passed parameter to decorator
        """
        def checkWallet(func):
            @wraps(func)
            def wrapper(*args,**kwargs):
                number=kwargs.get("number");
                found=getWallet(number);
                if found==True and exist==False:
                    raise WalletExist;
                elif found==False and exist==True:
                    raise WalletNotExist;
                
                