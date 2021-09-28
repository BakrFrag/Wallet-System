from rest_framework.exceptions import APIException 
class InternalServerError(APIException):
    """
    raised when internal server error happen
    """
    status_code=500;
    default_detail="internal server error"
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

class PhoneNumberValidationError(APIException):
    """
    raise when invalid phone number format
    """
    status_code=400;
    default_detail="invalid phone number format , phone number mst be 11 number and must start with 01";
class WalletPasswordVlidationError(APIException):
    """
    raise when invalid wallet password number
    """
    status_code=400;
    default_detail="invalid wallet password , wallet password mut be 6 numbers only";

class WalletPasswordError(APIException):
    """
    raise when parsed wallet password
    """
    status_code=400;
    default_detail="error wallet password"
class CreditWalletException(APIException):
    """
    raised when cedit wallet with amout <= 0
    """
    status_code=400;
    default_detail="wallet credit amount must be greater than 0";

class DebitWalletException(APIException):
    """
    raised whn debit amount > wallet balance
    """
    status_code=400;
    default_detail="wallet debit amount must be less than wallet balance";

class UnknownPropertyError(APIException):
    """
    raised when required property not attribute of wallet
    """
    status_code=400;
    default_detail="unkown property of wallet";