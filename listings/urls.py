from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    #path('<int:bid_id>', views.listing, name='bid'),
    path('search', views.search, name='search'),
    path('create', views.create, name='create'),
    path('list.json', views.get_rest_list, name='list'),
    #path('create', views.ProductCreateView.as_view(), name='create'),
]
