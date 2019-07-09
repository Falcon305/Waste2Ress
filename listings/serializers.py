from rest_framework import serializers
from .models import Listing


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('id', 'title', 'photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6', 'description', 'quantity', 
                'category', 'price', 'is_published', 'address', 'city', 'state', 'zipcode', 'delivery')