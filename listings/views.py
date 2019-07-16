from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
from .choices import price_choices, quantity_choices, state_choices
from django.contrib.auth.decorators import login_required
from accounts.models import User, Seller, Buyer
from accounts.decorators import buyer_required, seller_required
from django.utils import timezone
from .forms import ProductForm
from django.views.generic.edit import FormView, CreateView
from django.utils.decorators import method_decorator
from .models import Listing
from .serializers import ProductSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages, auth
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
from django.views.generic import UpdateView, DeleteView


# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-date_posted').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings' :paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    # seller = get_object_or_404(Seller, first_name=first_name)
    context = {
        'listing':listing,
        # 'seller': seller
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-date_posted')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
                 queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # quntity
    if 'quntity' in request.GET:
        quntity = request.GET['quntity']
        if quntity:
            queryset_list = queryset_list.filter(quntity__lte=quntity)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices,
        'quantity_choices': quantity_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)


@login_required
@seller_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['description'] and request.POST['quantity'] and request.FILES['photo_main'] and request.FILES['photo_1'] and request.FILES['photo_2'] and request.FILES['photo_3'] and request.FILES['photo_4'] and request.FILES['photo_5'] and request.FILES['photo_6'] and request.POST['category'] and request.POST['price'] and request.POST['address'] and request.POST['city'] and request.POST['state'] and request.POST['zipcode'] and request.POST['delivery'] :
            product = Listing()
            product.title = request.POST['title']
            product.photo_main = request.FILES['photo_main']
            product.photo_2 = request.FILES['photo_2']
            product.photo_3 = request.FILES['photo_3']
            product.photo_4 = request.FILES['photo_4']
            product.photo_5 = request.FILES['photo_5']
            product.photo_6 = request.FILES['photo_6']
            product.description = request.POST['description']
            product.quantity = request.POST['quantity']
            product.category = request.POST['category']
            product.city = request.POST['city']
            product.zipcode = request.POST['zipcode']
            product.address = request.POST['address']
            product.delivery = request.POST['delivery']
            product.price = request.POST['price']
            
            
            product.seller = request.user
            product.save()
            messages.success(request, 'You are now registered and can log in')
            return redirect('listings')
        else :
            messages.error(request, 'Fill in all the requerd Fields')
            return render(request, 'listings/create.html')
            
    else :
        return render(request, 'listings/create.html')

# @method_decorator(login_required, name='dispatch')
# @method_decorator(seller_required, name='dispatch')
# class ListingDeleteView(DeleteView):
#     model = Listing
#     success_url = '/'
#     template_name = 'listings/listing_confirm_delete.html'
#     def test_func(self):
#         listing = self.get_object()
#         if self.request.user == listing.seller:
#             return True
#         return False


@login_required
@seller_required
def listing_delete(request, pk):
    template = 'listings/listing_confirm_delete.html'
    listing = get_object_or_404(Listing, pk=pk)
    if request.user == listing.seller:
        listing.delete()
        return redirect('listings')
    context = {'listing': listing}
    return render(request, template, context)

@login_required
@seller_required
def listing_update(request, pk):
    instance = get_object_or_404(Listing, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=instance)
    if request.user == instance.seller:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Your Product has been updated successfully')
            return redirect('listings')
    context = {
        'title': instance.title,
        'listing': instance,
        'form': form,
    }
    return render(request, 'listings/update.html', context)    
    


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_rest_list(request):
    """
    Returns Json list of all restaurants
    """
    if request.method == "GET":
        rest_list = Listing.objects.order_by('-date_posted')
        serializer = ProductSerializer(rest_list, many=True)
        return JsonResponse(serializer.data, safe=False)

class ProductSerializerView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, status=Invoice.SENT)
        return Response(status=status.HTTP_201_CREATED)