from django import forms
from django.forms import ModelForm
from .models import Listing


class ProductForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6', 'description', 'quantity', 
                'category', 'price', 'is_published', 'address', 'city', 'state', 'zipcode', 'delivery']