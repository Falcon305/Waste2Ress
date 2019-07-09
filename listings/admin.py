from django.contrib import admin
from .models import Listing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published','category', 'price' , 'date_posted' ,'seller')
    list_display_links = ('id', 'title')
    list_filter = ('seller',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price', 'category')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)
'''admin.site.register(Auction)
admin.site.register(Watchlist)
admin.site.register(Chat)
admin.site.register(Bid)'''

