from django.db import models
from datetime import datetime
# Create your models here.

class Seller(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    email = models.EmailField()
    firstname = models.CharField(max_length=56)
    lastname = models.CharField(max_length=45)
    cellphone = models.CharField(max_length=14)
    address = models.CharField(max_length=255)
    town = models.CharField(max_length=45)
    post_code = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_mvp = models.BooleanField(default=False)
    join_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.username