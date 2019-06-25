from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from accounts.models import User, Buyer, Seller


class SellerSignUpForm(UserCreationForm):


    class Meta(UserCreationForm.Meta):
        model = User


    @transaction.atomic
    def save(self, commit=True):
    	user = super().save(commit=False)
    	user.is_seller = True
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