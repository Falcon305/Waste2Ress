from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from .decorators import seller_required, buyer_required
from .forms import SellerSignUpForm, BuyerSignUpForm
from .models import Seller, Buyer, User
from django.contrib import messages, auth


class SignUpView(TemplateView):
    template_name = 'accounts/register.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_buyer:
            return redirect('index')
        else:
            return redirect('listings')
    return render(request, 'index')



class BuyerSignUpView(CreateView):
    model = User
    form_class = BuyerSignUpForm
    template_name = 'accounts/register_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'buyer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

class SellerSignUpView(CreateView):
    model = User
    form_class = SellerSignUpForm
    template_name = 'accounts/register_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'seller'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('listings')

@login_required
@seller_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')