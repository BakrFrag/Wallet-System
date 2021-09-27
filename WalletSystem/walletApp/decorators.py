import re;
from functools import wraps
from django.contrib.auth.hashers import check_password;
from .exceptions import WalletExist;
from .helpers import getWallet;
from .exceptions import *;
from .helpers import getWallet;
from .validators import *;

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
                found=getWallet(phone).get("exists");
                print("phone:",phone);
                print("found:",found)
                if found==True and exist==False:
                    raise WalletExist;
                elif found==False and exist==True:
                     raise WalletNotExist;
                return func(*args,**kwargs);
            return wrapper;
        return checkWallet;
                
def checkPhoneNumberFormat(func):
    """
    add decorator to check phone validation
    """
    def wrapper(*args,**kwargs):
        phone=args[1].data.get("phone");
        if re.match(phone_number_pattern,phone):
            return func(*args,**kwargs);
        raise PhoneNumberValidationError;
    return wrapper;

def checkWalletPasswordFormat(func):
    """
    decorator to check wallet password must be 6 numbers only
    """
    def wrapper(*args,**kwargs):
        password=args[1].data.get("password");
        if re.match(wallet_password_pattern,password):
            return func(*args,**kwargs);
        raise WalletPasswordVlidationError
    return wrapper;

def checkWalletPassword(func):
    """
    decorator to check if wallet password correct
    """
    def wrapper(*args,**kwargs):
        phone=args[1].data.get("phone");
        wallet=getWallet(phone);
        print("function result:",wallet)
        parsed_password=args[1].data.get("password");
        wallet_password=wallet.get("wallet").password;
        print("parsed:",parsed_password);
        print("already:",wallet_password)
        print(check_password(parsed_password,wallet_password))
        if check_password(parsed_password,wallet_password):
            return func(*args,**kwargs);
        raise WalletPasswordError;
    return wrapper;

def checkWalletActivation(status):
    """
    decorator to check if walet is activated or not
    """
    def checkActivation(func):
        def wrapper(*args,**kwargs):
            phone=args[1].data.get("phone");
            wallet=getWallet(phone).wallet;
            if wallet.is_active and status==False:
                raise WalletAlreadyActivated;
            elif wallet.is_acive==False and status==True:
                raise WalletNotActivated
            return func(*args,**kwargs);
        return wrapper;
    return checkActivation; 