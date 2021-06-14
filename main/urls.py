from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth.views import * 


urlpatterns = [
	path('', main_handler, name='main_handler'),
	path('test/', test, name='test'),
	path('register/', register_user, name='register_user'),
	path('buy_money/', buy_money, name='buy_money'),
	path('buy_boost_x8/', buy_boost_x8, name='buy_boost_x8'),
	path('profile/', profile, name='profile')
	# path('login/', LoginView.as_view(), name='login'),
	# path('logout/', LogoutView.as_view(), name='logout'),	
]