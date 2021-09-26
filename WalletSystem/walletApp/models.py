from django.db import models
from django.core.validators import RegexValidator;
from .validators import *
# Create your models here.
class Wallet(models.Model):
    """
    include all nessasry fields for creating , mainuplations wallet
    """
    phone=models.CharField(max_length=13,validators=[RegexValidator(phone_number_pattern,"wallet phone number must be 11 digits")]);
    balance=models.FloatField(default=0.0);
    password = models.CharField(max_length=6,validators=[RegexValidator(wallet_password_pattern,"wallet password must be 6 numbers")]);
    is_active = models.BooleanField(default=False)