import re;
from functools import wraps
from .exceptions import WalletExist;
from .helpers import getWallet;
from .exceptions import *;
from .helpers import getWallet;


def checkWalletExistance(exist):
        """
        check wallet exists or not according to passed parameter to decorator
        """
        def checkWallet(func):
            @wraps(func)
            def wrapper(*args,**kwargs):
                print("kwargs:",kwargs);
                data=args[1].data;
                phone=data.get("phone");
                found=getWallet(phone);
                print("phone:",phone);
                print("found:",found)
                if found==True and exist==False:
                    raise WalletExist;
                elif found==False and exist==True:
                     raise WalletNotExist;
                return func(*args,**kwargs);
            return wrapper;
        return checkWallet;
                
