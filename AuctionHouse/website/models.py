from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class AuctionItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    current_bid_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True, related_name='bids_made')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auction_items_created')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    image = models.ImageField(upload_to='auction_item_images/', blank=True, null=True)

    def is_live(self):
        return self.start_time <= timezone.now() <= self.end_time

    def is_upcoming(self):
        return self.start_time > timezone.now()

    def is_past(self):
        return self.end_time < timezone.now()

    def __str__(self):
        return self.title
