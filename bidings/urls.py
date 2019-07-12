from django.urls import path
from . import views

urlpatterns = [
    path('bid/<int:listing_id>/', views.bid_index, name='bid'),
    path('save_bid/<int:listing_id>/', views.save_bid, name='save_bid'),
]