from django.db import models
from datetime import datetime
from accounts.models import Seller, Buyer, User
# Create your models here.

'''class Listing(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING),
    title = models.CharField(max_length=255),
    address = models.CharField(max_length=255),
    city = models.CharField(max_length=255),
    state = models.CharField(max_length=255),
    zipcode = models.CharField(max_length=255),
    description = models.TextField(blank=True),
    price = models.IntegerField(),
    category = models.CharField(max_length=255),
    quantity = models.CharField(max_length=255),
    delivery = models.CharField(max_length=255),
    dead_line = models.CharField(max_length=255),
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d'),
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True),
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True),
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True),
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True),
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True),
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True),
    is_published = models.BooleanField(default=True),
    list_date = models.DateTimeField(default=datetime.now, blank=True),'''

class Listing(models.Model):
    CATEGORIES = (
        ('CW', 'Construction waste'),
        ('ET', 'Electronics'),
        ('GLS', 'Glass'),
        ('HAZ', 'Hazardous'),
        ('FER', 'Metals'),
        ('HAZ', 'Hazardous'),
        ('MWP', 'Mixed waste products'),
        ('ORG', 'Organic'),
        ('PAC', 'Paper and cardboard'),
        ('MK', 'Plastics'),
        ('RUB', 'Rubber'),
        ('TOB', 'Textiles')
    )
    title = models.CharField(max_length=255)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    quantity = models.IntegerField()
    category = models.CharField(
        max_length=3,
        choices=CATEGORIES
    )
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)
    seller = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    price = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255 )
    delivery = models.CharField(max_length=255)

    def __str__(self):
        return self.title
        
class Auction(models.Model):
    listing_id = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    number_of_bids = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    time_ending = models.DateTimeField()
    staring_price = models.IntegerField(default=0)

class Watchlist(models.Model):
    user_id = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)

class Bid(models.Model):
    user_id = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bid_time = models.DateTimeField(auto_now_add=True, blank=True)

class Chat(models.Model):
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    time_sent = models.DateTimeField()