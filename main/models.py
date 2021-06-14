from django.db import models
from django.contrib.auth.models import *

class MyUser(AbstractUser):
	email = models.EmailField(max_length=20, default='', blank=False)
	username = models.CharField(max_length=100, unique=True)
	money_all_times = models.IntegerField(default=0)
	balance = models.IntegerField(default=0)
	boosts_x2 = models.BooleanField(default=False)
	boosts_x3 = models.BooleanField(default=False)
	boosts_x4 = models.BooleanField(default=False)
	boosts_x5 = models.BooleanField(default=False)
	boosts_x8 = models.BooleanField(default=False)
	boosts_x10 = models.BooleanField(default=False)
	boosts_x15 = models.BooleanField(default=False)
	boost_unable = models.CharField(max_length=50, default='')
	clicks_now = models.IntegerField(default=0)
	quantity_clicks = models.IntegerField(default=0)

	def __str__(self):
		return self.username
