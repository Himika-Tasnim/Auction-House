# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import AuctionItem
from .forms import AuctionSearchForm, AuctionItemForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def live_auction_items(request):
    current_time = timezone.now()
    # Live Auctions
    live_auctions = AuctionItem.objects.filter(start_time__lte=current_time, end_time__gte=current_time)

    return render(request, 'live_auction_items.html', {
        'live_auctions': live_auctions,
    })

def upcoming_auction_items(request):
    current_time = timezone.now()

    upcoming_auctions = AuctionItem.objects.filter(start_time__gt=current_time, end_time__gt=current_time)

    return render(request, 'upcoming_auction_items.html', {
        'upcoming_auctions': upcoming_auctions,
    })


def auction_detail(request, item_id):
    auction_detail = get_object_or_404(AuctionItem, id=item_id)
    return render(request, 'auction_detail.html', {'auction_detail': auction_detail})


def search_live_auctions(request):
    query = request.GET.get('query', '')
    current_time = timezone.now()

    # checks if the query is in the title or address of the auction item
    live_auctions = AuctionItem.objects.filter(
        Q(title__icontains=query) | Q(address__icontains=query),
        start_time__lte=current_time, 
        end_time__gte=current_time
    )

    return render(request, 'auction_search.html', {'auctions': live_auctions, 'query': query, 'search_type': 'Live Auctions'})

def search_upcoming_auctions(request):
    query = request.GET.get('query', '')
    current_time = timezone.now()

    upcoming_auctions = AuctionItem.objects.filter(
        Q(title__icontains=query) | Q(address__icontains=query),
        start_time__gt=current_time,
        end_time__gt=current_time
    )

    return render(request, 'auction_search.html', {'auctions': upcoming_auctions, 'query': query, 'search_type': 'Upcoming Auctions'})

@login_required 
def create_auction(request):
    if request.method == 'POST':
        form = AuctionItemForm(request.POST, request.FILES)
        if form.is_valid():
            auction_item = form.save(commit=False)
            auction_item.created_by = request.user
            auction_item.save()
            return redirect('auction_detail', item_id=auction_item.id)
    else:
        form = AuctionItemForm()

    return render(request, 'create_auction.html', {'form': form})

