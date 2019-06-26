from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from accounts.models import Seller
from listings.choices import price_choices, quantity_choices, state_choices

# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-date_posted').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'quantity_choices': quantity_choices,
        'price_choices': price_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    # Get All Sellers
    sellers = Seller.objects.order_by('join_date')
    # Get MVP
    mvp_sellers = Seller.objects.all().filter(is_mvp=True)
    context = {
        'sellers': sellers,
        'mvp_sellers': mvp_sellers
    }
    return render(request, 'pages/about.html', context)