from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
    path('create', views.create, name='create'),
    #path('create', views.ProductCreateView.as_view(), name='create'),
]
