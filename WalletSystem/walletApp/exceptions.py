from rest_framework.exceptions import APIException 
class WalletExist(APIException):
    """
    raised when creating wallet while wallet already exist
    """
    status_code=400;
    default_detail="wallet with this phone number already exist";
class WalletNotExist(APIException):
    """
    raised when wallet not exist
    """
    status_code=400;
    default_detail="wallet with this phone number not exist";

class WalletNotActivated(APIException):
    """
    rasied when wallet not activated
    """
    status_code=400;
    default_detail="wallet not Activated yet";
class WalletAlreadyActivated(APIException):
    """
    raised when wallet already activated
    """
    status_code=400;
    default_detail="wallet Already Activated";