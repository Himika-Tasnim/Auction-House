from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator

class Buyer_Seller(models.Model):
    user=models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    phone=models.CharField(max_length=11)
    address=models.CharField(max_length=100)
    ratings_sum = models.IntegerField(default=0)
    ratings_count = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    def average_rating(self):
        if self.ratings_count == 0:
            return 0
        return self.ratings_sum / self.ratings_count

