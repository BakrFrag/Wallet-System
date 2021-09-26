import re;
from functools import wraps
from wallet.exceptions import WalletExist;

from .exceptions import *;
from .helpers import getWallet;


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
                
                