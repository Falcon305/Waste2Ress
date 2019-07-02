from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from accounts.models import User, Buyer, Seller


class SellerSignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=255 , required=True)
    last_name = forms.CharField(max_length=255)
    cellphone = forms.CharField(max_length=14)
    address = forms.CharField(max_length=255)
    town = forms.CharField(max_length=45)
    post_code = forms.CharField(max_length=45)
    country = forms.CharField(max_length=45)
    #photo = forms.ImageField()
    class Meta(UserCreationForm.Meta):
        model = User


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_seller = True
        #user.first_name = first_name
        user.save()
        seller = Seller.objects.create(user=user)
        seller.email = self.cleaned_data["email"]
        seller.first_name = self.cleaned_data["first_name"]
        seller.last_name = self.cleaned_data["last_name"]
        seller.cellphone = self.cleaned_data["cellphone"]
        seller.address = self.cleaned_data["address"]
        seller.town = self.cleaned_data["town"]
        seller.post_code = self.cleaned_data["post_code"]
        seller.country = self.cleaned_data["country"]
        #seller.photo = self.cleaned_data["photo"]
        #seller.first_name.add(*self.cleaned_data.get('first_name'))
        seller.save()
        return user


class BuyerSignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=255 , required=True)
    last_name = forms.CharField(max_length=255)
    cellphone = forms.CharField(max_length=14)
    address = forms.CharField(max_length=255)
    town = forms.CharField(max_length=45)
    post_code = forms.CharField(max_length=45)
    country = forms.CharField(max_length=45)
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_buyer = True
        user.save()
        buyer = Buyer.objects.create(user=user)
        seller = Seller.objects.create(user=user)
        buyer.email = self.cleaned_data["email"]
        buyer.first_name = self.cleaned_data["first_name"]
        buyer.last_name = self.cleaned_data["last_name"]
        buyer.cellphone = self.cleaned_data["cellphone"]
        buyer.address = self.cleaned_data["address"]
        buyer.town = self.cleaned_data["town"]
        buyer.post_code = self.cleaned_data["post_code"]
        buyer.country = self.cleaned_data["country"]
        buyer.save()
        return user