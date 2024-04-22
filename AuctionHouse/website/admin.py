from django.contrib import admin
from .models import *

admin.site.register(AuctionItem, AuctionItemAdmin)
admin.site.register(Wishlist)
admin.site.register(Bid)