from django.contrib import admin
from .models import Seller
# Register your models here.

class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'firstname', 'lastname', 'is_mvp','email', 'join_date')
    list_display_links = ('id', 'username')
    search_fields = ('username', 'firstname', 'lastname')
    list_per_page = 25

admin.site.register(Seller, SellerAdmin)