import re;
from functools import wraps;
from .models import Wallet
phone_number_pattern=re.compile(r"(\+2)?([0-9]{11})$")
wallet_password_pattern=re.compile(r"([0-9]{6})$");
def checkWalletExistance(exist):
        """
        check wallet exists or not according to passed parameter to decorator
        """
        def checkWallet(func):
            @wraps(func)
            def wrapper(*args,**kwargs):
                wallet=kwargs.get("wallet");
                db=kwargs.get("db")
                obj=get_wallet_object(db,wallet);
                if exist== False and obj.get("exist")==True:
                    raise HTTPException(status_code=400, detail="Wallet With This Phone Number Exists");
                
                elif exist==True and obj.get("exist")==False:
                    raise HTTPException(status_code=400, detail="No Wallet With This Phone Number");
                return func(*args,**kwargs);
            return wrapper;
        return checkWallet;