from django.shortcuts import render
from .models import *
from django.http import *
from .forms import *
import json


def test(request):
	usr = MyUser.objects.get(id=request.user.id)

	data = request.GET['post_id']
	if data == 'yes':
		usr = MyUser.objects.get(id=request.user.id)
		print(usr.username)
		if usr.quantity_clicks >= 200 and usr.quantity_clicks <= 500:
			usr.boosts_x2 = True
			usr.boost_unable = 'x2'

		if usr.quantity_clicks >= 500 and usr.quantity_clicks <= 1000:
			usr.boosts_x3 = True
			usr.boost_unable = 'x3'

		if usr.quantity_clicks >= 1000:
			usr.boosts_x4 = True
			usr.boost_unable = 'x4'


				
		kof = 1		
			
		if usr.boost_unable == '':
			pass
		if usr.boosts_x2 == True:
			kof = 2
		if usr.boosts_x3 == True:
			kof = 3
		if usr.boosts_x4 == True:
			kof = 4
		if usr.boosts_x8 == True:
			kof = 8
		if usr.boosts_x10 == True:
			kof = 10
		if usr.boosts_x15 == True:
			kof = 15						

		if usr.boost_unable == '':
			boost = ''
			pass
		if usr.boosts_x2 == True:
			boost = 'x2'
		if usr.boosts_x3 == True:
			boost = 'x3'
		if usr.boosts_x4 == True:
			boost = 'x4'
		if usr.boosts_x8 == True:
			boost = 'x8'
		if usr.boosts_x10 == True:
			boost = 'x10'
		if usr.boosts_x15 == True:
			boost = 'x15'

		print(usr.boost_unable)		
		print(kof)
		usr.clicks_now += (1 * kof)
		usr.quantity_clicks += (1 * kof)
		usr.save()

	print('сейчас:', usr.clicks_now, '---', 'всего:', usr.quantity_clicks)
	data = {'now': usr.clicks_now, 'all_time': usr.quantity_clicks, 'boosts': boost}
	return HttpResponse(json.dumps(data))

def buy_money(request):
	data = request.GET['data']
	if data == 'yes':
		usr = MyUser.objects.get(id=request.user.id)

		if usr.clicks_now < 1000:
			return HttpResponse(json.dumps({'success': 'no'}))	
		

		usr.clicks_now -= 1000

		usr.money_all_times += 1
		usr.balance += 1

		usr.save()

	return HttpResponse(json.dumps(usr.balance))

def buy_boost_x8(request):
	data = request.GET['data']
	if data == 'x8':
		usr = MyUser.objects.get(id=request.user.id)
		if usr.boosts_x8 == True:
		    return HttpResponse(json.dumps({'v': 'yes'}))
		elif usr.balance >= 5:
			usr.boost_unable = 'x8'
			usr.balance -= 5
			usr.boosts_x8 = True
			usr.save()
			print(usr.boost_unable)
			return HttpResponse(json.dumps(usr.balance))
		elif usr.balance < 5:
			return HttpResponse(json.dumps({'v': 'no'}))
	
	elif data == 'x10':
		usr = MyUser.objects.get(id=request.user.id)
		
		if usr.boosts_x10 == True:
		    return HttpResponse(json.dumps({'v': 'yes'}))
		elif usr.balance >= 10:
			usr.boost_unable = 'x10'
			usr.balance -= 10
			usr.boosts_x10 = True
			usr.save()
			print(usr.boost_unable)
			return HttpResponse(json.dumps(usr.balance))
		elif usr.balance < 10:
			return HttpResponse(json.dumps({'v': 'no'}))
	elif data == 'x15':
		usr = MyUser.objects.get(id=request.user.id)
		
		if usr.boosts_x15 == True:
		    return HttpResponse(json.dumps({'v': 'yes'}))
		elif usr.balance >= 15:
			usr.boost_unable = 'x15'
			usr.balance -= 15
			usr.boosts_x15 = True
			usr.save()
			print(usr.boost_unable)
			return HttpResponse(json.dumps(usr.balance))
		elif usr.balance < 15:
			return HttpResponse(json.dumps({'v': 'no'}))											

def main_handler(request):
	try:
		usr = MyUser.objects.get(id=request.user.id)

		print(usr.boost_unable)
		counts = usr.clicks_now
		money = usr.balance	
		counts_all_time = usr.quantity_clicks
		if usr.boost_unable == '':
			boost = ''
			pass
		if usr.boosts_x2 == True:
			boost = 'x2'
		if usr.boosts_x3 == True:
			boost = 'x3'
		if usr.boosts_x4 == True:
			boost = 'x4'
		if usr.boosts_x8 == True:
			boost = 'x8'
		if usr.boosts_x10 == True:
			boost = 'x10'
		if usr.boosts_x15 == True:
			boost = 'x15'

		print(usr.clicks_now, usr.quantity_clicks, usr.money_all_times, usr.balance)

		return render(request, 'main/index.html', {'counts': counts, 'money': money, 'counts_all_time': counts_all_time, 'boost': boost})
	except:
		return render(request, 'main/index.html', {'counts': 0, 'money': 0, 'counts_all_time': 0})	
			
def register_user(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)  
        if user_form.is_valid():
            
            new_user = user_form.save(commit=False)
            
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            
			
            return render(request, 'main/register_done.html', {'new_user': new_user})
    else:
		
        user_form = UserRegistrationForm()
	
    return render(request, 'register/register.html', {'user_form': user_form})

def profile(request):
	usr = MyUser.objects.get(id=request.user.id)
	if usr.boost_unable == '':
		boost = ''
		pass
	if usr.boosts_x2 == True:
		boost = 'x2'
	if usr.boosts_x3 == True:
		boost = 'x3'
	if usr.boosts_x4 == True:
		boost = 'x4'
	if usr.boosts_x8 == True:
		boost = 'x8'
	if usr.boosts_x10 == True:
		boost = 'x10'
	if usr.boosts_x15 == True:
		boost = 'x15'

	return render(request, 'main/cabinet.html', {'boost': boost})