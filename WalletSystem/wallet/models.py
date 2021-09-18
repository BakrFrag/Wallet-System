from django.db import models
from django.db.models.fields import FloatField

# Create your models here.
class Wallet(models.Model):
    """
    include all nessasry fields for creating , mainuplations wallet
    """
    phone=models.CharField(max_length=13);
    balance=models.FloatField(default=0.0);
    password = models.CharField(max_length=6);
    is_active = models.BooleanField(default=False)