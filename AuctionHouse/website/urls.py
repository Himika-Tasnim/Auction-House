from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('live-auction-items/', views.live_auction_items, name='live_auction_items'),
    path('upcoming-auction-items/', views.upcoming_auction_items, name='upcoming_auction_items'),
    path('auction-detail/<int:item_id>/', views.auction_detail, name='auction_detail'),
    path('search-live-auctions/', views.search_live_auctions, name='search_live_auctions'),
    path('search-upcoming-auctions/', views.search_upcoming_auctions, name='search_upcoming_auctions'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)