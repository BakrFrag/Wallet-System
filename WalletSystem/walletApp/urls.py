from django.urls import path;
from rest_framework.urlpatterns import format_suffix_patterns;
from .views import WalletViewset;
create_wallet=WalletViewset.as_view({
    "post":"create_wallet"
});
urlpatterns = format_suffix_patterns([
        path("create/",create_wallet,name="create_wallet"),
    ])
   

