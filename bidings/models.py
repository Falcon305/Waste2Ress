from django.db import models
from listings.models import Listing
from accounts.models import Seller, Buyer, User
# Create your models here.

class Bid(models.Model):
    STATUS_ = (
        ('W', 'Wining'),
        ('L', 'Losing'),
    )
    user_id = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    product = models.ForeignKey(Listing, on_delete=models.CASCADE)
    bid_time = models.DateTimeField(auto_now_add=True, blank=True)
    amount = models.FloatField()
    status = models.CharField(max_length=1, choices=STATUS_, blank=True)
    

    def __str___(self):
        return self.id

'''class P_History(models.Model):
    product = models.ForeignKey(Product)
    bidder_name = models.CharField(max_length= 30)
    bidded_time = models.TimeField(default= timezone.now())
    bidded_price =models.DecimalField(max_digits = 14, decimal_places=2, default=0.00)

    def __str__(self):
        return self.product.nam'''