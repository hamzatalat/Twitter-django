from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import User
from .models import Tweets , likes , comments,follow

def Home(request, ids):
    o = User.objects.get(id=ids)
    return render(request, 'tweets/home.html',{'o' : o})


def posttweet(request, ids):
    o = User.objects.get(id=ids)
    return render(request, 'tweets/posttweet.html',{'o' : o})

def savetweet(request , ids):
	if request.method == 'POST':
		o = User.objects.get(id=ids)	
		my_model = Tweets()	
		string = request.POST['tweettext']
		my_model.tweet=string
		my_model.tweeted_by=o
		my_model.save()


def finduser(request , ids):
	o = User.objects.get(id=ids)
	return render(request, 'tweets/finduser.html',{'o' : o})



def fonduser(request , ids):
	if request.method == 'POST':
		o = User.objects.get(id=ids)	
		string = request.POST['find_user']
		try:		
			finduser = User.objects.get(name=string)
			o={'o':o , 'a':finduser}
			return render(request, 'tweets/founduserdetails.html' , o)
		except User.DoesNotExist:	
			pass


def followuser(request , ids, aids):
	if request.method == 'POST':
		o = User.objects.get(id=ids)
		o2 = User.objects.get(id=aids)	
		db =follow()
		db.user=o
		db.followed_by=o2
		db.save()


def viewtweets (request , ids):
	o = User.objects.get(id=ids)
	o2 = follow.objects.filter(user=ids)
	a=[]
	for itr in o2 :
		a.append(User.objects.get(id=itr.followed_by.id))
	o = {'o' : o ,'a': a}
	return render(request, 'tweets/viewtweets.html', o )



def liketweet(request , ids, aids):
	obj = User.objects.get(id=ids)
	o=likes()
	o.liked_by=obj
	obj1 = Tweets.objects.get(tweet=aids)
	o.tweet = obj1
	try:	
		if likes.objects.get(liked_by=o.liked_by ,tweet = o.tweet) :
			return render(request, 'tweets/likeunsuccesfull.html')
				
	except:
		o.save()
		return render(request, 'tweets/likesuccesfull.html' )

def commenttweet(request , ids, aids):
	if request.method == 'POST':	
		obj = User.objects.get(id=ids)
		o=comments()
		o.commented_by=obj
		obj = Tweets.objects.get(tweet=aids)
		o.tweet = obj
		string = request.POST['comment']
		o.comment=string
		o.save()















