from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from crispy_forms.helper import FormHelper
from django.forms.utils import ValidationError

from accounts.models import User, Buyer, Seller


class SellerSignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=255 , required=True, widget=forms.TextInput(attrs={'placeholder': 'Fisrt Name', 'class':' form-control login-input'}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class':' form-control login-input'}))
    cellphone = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Phone Number', 'class':' form-control login-input'}))
    address = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Address', 'class':' form-control login-input'}))
    town = forms.CharField(max_length=45, widget=forms.TextInput(attrs={'placeholder': 'City', 'class':' form-control login-input'}))
    post_code = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Zip Code', 'class':' form-control login-input'}))
    country = forms.CharField(max_length=45, widget=forms.TextInput(attrs={'placeholder': 'Country', 'class':' form-control login-input'}))
    def __init__(self, *args, **kwargs):
        super(SellerSignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.fields['username'].widget.attrs.update({'placeholder': 'Username', 'class':' form-control'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password', 'class':' form-control login-input'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Password Confirmation', 'class':' form-control login-input'})
        self.fields['email'].widget.attrs.update({'placeholder': 'email', 'class':' form-control login-input'})
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
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
    first_name = forms.CharField(max_length=255 , required=True , widget=forms.TextInput(attrs={'placeholder': 'Fisrt Name', 'class':' form-control login-input'}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class':' form-control login-input'}))
    cellphone = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Phone Number', 'class':' form-control login-input'}))
    address = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Address', 'class':' form-control login-input'}))
    town = forms.CharField(max_length=45, widget=forms.TextInput(attrs={'placeholder': 'City', 'class':' form-control login-input'}))
    post_code = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Zip Code', 'class':' form-control login-input'}))
    country = forms.CharField(max_length=45, widget=forms.TextInput(attrs={'placeholder': 'Country', 'class':' form-control login-input'}))

    def __init__(self, *args, **kwargs):
        super(BuyerSignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.fields['username'].widget.attrs.update({'placeholder': 'Username', 'class':' form-control login-input'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password', 'class':' form-control login-input'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Password Confirmation', 'class':' form-control login-input'})
        self.fields['email'].widget.attrs.update({'placeholder': 'email', 'class':' form-control login-input'})
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
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