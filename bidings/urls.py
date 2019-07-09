from django.urls import path
from . import views

urlpatterns = [
    path('bid', views.bid, name='bid'),
]