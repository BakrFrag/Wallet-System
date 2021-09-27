from django.urls import path;
from rest_framework.urlpatterns import format_suffix_patterns;
from .views import WalletViewset;
create_wallet=WalletViewset.as_view({
    "post":"create_wallet"
});
activate_wallet=WalletViewset.as_view({
    "post":"activateWallet"
});
get_wallet_balance=WalletViewset.as_view({
    "get":"getWalletBalance"
});
debit_wallet=WalletViewset.as_view({
    "put":"debitWalletBalance"
});
credit_wallet=WalletViewset.as_view({
    "put":"creditWalleBalance"
});
urlpatterns = format_suffix_patterns([
        path("create/",create_wallet,name="create_wallet"),
        path("activate/",activate_wallet,name="activate_wallet"),
        path("balance/",get_wallet_balance,name="wallet_balnce"),
        path("credit/",credit_wallet,name="credit_wallet"),
        path("debit/",debit_wallet,name="debit_wallet")
    ])
   

