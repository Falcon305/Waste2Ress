from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
#from listings.models import Listing
#from listings.models import Auction

class User(AbstractUser):
    is_buyer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)

class Seller(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	first_name = models.CharField(max_length=255)
	email = models.EmailField()
	last_name = models.CharField(max_length=255)
	cellphone = models.CharField(max_length=14)
	address = models.CharField(max_length=255)
	town = models.CharField(max_length=45)
	post_code = models.CharField(max_length=45)
	country = models.CharField(max_length=45)
	photo = models.ImageField(upload_to='photos/%Y/%m/%d')
	is_mvp = models.BooleanField(default=False)
	join_date = models.DateTimeField(auto_now_add=True, blank=True)
	def __str__(self):
		return self.first_name
class Buyer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	first_name = models.CharField(max_length=255)
	email = models.EmailField()
	last_name = models.CharField(max_length=255)
	cellphone = models.CharField(max_length=14)
	address = models.CharField(max_length=255)
	town = models.CharField(max_length=45)
	post_code = models.CharField(max_length=45)
	country = models.CharField(max_length=45)
	photo = models.ImageField(upload_to='photos/%Y/%m/%d')
	join_date = models.DateTimeField(auto_now_add=True, blank=True)
	#number_of_bids = models.IntegerField(_(""))
	#auctions_list = models.ManyToManyField("listings.Auction", blank=True)
	
	def __str__(self):
		return self.user.username