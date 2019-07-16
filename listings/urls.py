from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    #path('<int:bid_id>', views.listing, name='bid'),
    path('search', views.search, name='search'),
    path('create', views.create, name='create'),
    path('list.json', views.get_rest_list, name='list'),
    #path('listings/<int:pk>/update/', views.ListingUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.listing_delete, name='delete'),
     path('<int:pk>/update/', views.listing_update, name='update'),
    #path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    #path('create', views.ProductCreateView.as_view(), name='create'),
]
