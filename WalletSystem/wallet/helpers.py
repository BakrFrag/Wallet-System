from .models import Wallet;
def getWallet(phone_number):
    """
    helper function check if wallet with phone number exists or not
    """
    try:
        Wallet.objects.get(phone=phone_number);
        return True;
    except ObjectDoesNotExist:
        return False;