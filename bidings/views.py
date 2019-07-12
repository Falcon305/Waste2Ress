from django.shortcuts import render, redirect,get_object_or_404, HttpResponseRedirect
from accounts.decorators import buyer_required, seller_required
from django.contrib.auth.decorators import login_required
from listings.models import Listing
from .models import Bid
from accounts.models import Buyer, User
from django.utils import timezone
from django.contrib import messages, auth
from django.urls import reverse
from django.contrib import messages, auth

# Create your views here.


@login_required
@buyer_required
def bid_index(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing':listing
    }
    return render(request, 'bid/bid.html', context)

def save_bid(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    field_name = 'price'
    #obj = Listing.objects.first()
    field_value = getattr(listing, field_name)
    print("price", field_value)
    if request.method == 'POST':
        am = int(request.POST['am'])
        if field_value > am :
            messages.error(request, 'Bid price must be more than munimun price')
            return render(request, 'bid/bid.html', {'listing':listing})
        else:
            bid = Bid()
            bid.amount = request.POST['am']
            bid.bid_time = timezone.datetime.now()
            bid.user_id = Buyer.objects.get(user=request.user)
            bid.product = listing
            bid.save()
            listing = Listing()
            listing.num_bids = int(listing.num_bids) + 1
        return redirect('listings')
    return render(request, 'bid/bid.html', {'listing':listing})