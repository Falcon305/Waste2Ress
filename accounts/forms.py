from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from accounts.models import User, Buyer, Seller


class SellerSignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    cellphone = forms.CharField()
    address = forms.CharField()
    town = forms.CharField()
    post_code = forms.CharField()
    country = forms.CharField()
    photo = forms.ImageField()
    class Meta(UserCreationForm.Meta):
        model = User


    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_seller = True
        #user.first_name = first_name
        user.save()
        seller = Seller.objects.create(user=user)
        return user


class BuyerSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_buyer = True
        user.save()
        buyer = Buyer.objects.create(user=user)
        return user


class SellerCompletForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ('first_name', 'last_name', 'cellphone', 'address', 'town', 'post_code', 'country', 'photo', 'email')