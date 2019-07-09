from django.shortcuts import render, redirect,get_object_or_404
from accounts.decorators import buyer_required, seller_required
from django.contrib.auth.decorators import login_required
from listings.models import Listing
from .models import Bid
from accounts.models import Buyer, User
from django.utils import timezone
from django.contrib import messages, auth

# Create your views here.


@login_required
@buyer_required
def bid(request):
    listing = get_object_or_404(Listing, pk=listing_id)
    '''context = {
        'listing':listing
    }'''
    if request.method == 'POST':
        if request.POST['am'] :
            bid = Bid()
            bid.amount = request.POST['am']
            bid.bid_time = timezone.datetime.now()
            bid.user_id = request.user
            bid.product = Listing.objects.get(pk=listing_id)
            bid.save()
            messages.success(request, 'Your offer has been regesterd successfully')
            return redirect('bid')
        else :
            messages.error(request, 'Fill in all the requerd Fields')
            return render(request, 'bid/bid.html')
            
    else :
        return render(request, 'bid/bid.html')

'''def history(request,product_id):
    p = Listing.objects.get(pk = product_id)
    ph = P_History.objects.filter(product =p)
    return render(request, 'history.html', {'ph': ph })'''