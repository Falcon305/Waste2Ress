from django.urls import path, include
from . import views

urlpatterns = [
	path(' ', include('django.contrib.auth.urls')),
    path('register', views.SignUpView.as_view(), name='register'),
    path('signup/buyer/', views.BuyerSignUpView.as_view(), name='buyer_register'),
    path('signup/seller/', views.SellerSignUpView.as_view(), name='seller_register'),
   # path('logout', views.logout, name='logout'),
    #path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),

]

