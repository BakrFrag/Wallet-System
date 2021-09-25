import re;
from functools import wraps
from wallet.exceptions import WalletExist;
from django.core.exceptions import ObjectDoesNotExist
from .models import Wallet;
from .exceptions import *;
from .helpers import getWallet;
phone_number_pattern=re.compile(r"(\+2)?([0-9]{11})$")
wallet_password_pattern=re.compile(r"([0-9]{6})$");

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
                
                