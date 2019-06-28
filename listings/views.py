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
    context = {
        'listing':listing
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

'''@login_required
@seller_required
def create(request, template_name="listings/create.html'"):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        return redirect('index')
    return render(request, 'listings/create.html', {'form': form})'''


'''@method_decorator([login_required, seller_required], name='dispatch')
class ProductCreateView(CreateView):
    model = Listing
    fields = ('title', 'photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6', 'description', 'quantity', 
                'category', 'price', 'is_published', 'address', 'city', 'state', 'zipcode', 'delivery')
    #form_class = ProductForm
    #success_url = 'index'
    template_name = 'listings/create.html'

    def form_valid(self, form):
            self.object = form.save(commit=False)
            self.user = self.request.user
            self.object.save()
            return redirect('listings')'''

@login_required
@seller_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['description'] and request.POST['quantity'] and request.FILES['photo_main'] and request.FILES['photo_1'] and request.FILES['photo_2'] and request.FILES['photo_3'] and request.FILES['photo_4'] and request.FILES['photo_5'] and request.FILES['photo_6'] and request.POST['category'] and request.POST['price'] and request.POST['address'] and request.POST['city'] and request.POST['state'] and request.POST['zipcode'] and request.POST['delivery'] :
            product = Listing()
            product.title = request.POST['title']
            product.photo_main = request.FILES['photo_main']
            product.photo_1 = request.FILES['photo_1']
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
            product.pub_date = timezone.datetime.now()
            product.seller = request.user
            product.save()
            return redirect('listings')
        else :
            return render(request, 'listings/create.html', {'error': 'All Fields are required'})
    else :
        return render(request, 'listings/create.html')
