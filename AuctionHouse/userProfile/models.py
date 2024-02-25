from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator

# Create your models here.
class Buyer_Seller(models.Model):
    user=models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    phone=models.CharField(max_length=11)
    address=models.CharField(max_length=100)
    def __str__(self):
        return self.user.username