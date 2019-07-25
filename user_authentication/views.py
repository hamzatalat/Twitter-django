from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import User

# Create your views here.

class Base(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'user/user.html'




class signin(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'user/signin.html'
    


def ChangeProfile(request, ids):
    return render(request, 'user/changeProfile.html',{'ids' : ids})


def savedata(request):
	my_model = User()
	string = request.POST['email_']
	if string != '':
		my_model.email = string
		if request.POST['pass_'] :
			my_model.password = request.POST['pass_']
			if request.POST['u_name'] :
				likesmy_model.name = request.POST['u_name']	
				try:
					if User.objects.get(email=my_model.email , password = my_model.password , name=my_model.name) :
						return render(request, 'user/signuperror.html')
				except:	
					my_model.save()
					return render(request, 'user/signupsuccesfull.html')
			else:
				return render(request, 'user/signuperror.html')
		else:
			return render(request, 'user/signuperror.html')
	else:
		return render(request, 'user/signuperror.html')

def updatedata(request,ids):
	if request.method == 'POST':
		o = User.objects.get(id=ids)	
		my_model = o
		string = request.POST['email_']
		my_model.email = string
		my_model.password = request.POST['pass_']
		my_model.name = request.POST['u_name']	
		my_model.save()
	else:
	   pass # For GET
	o = User.objects.get(id=ids)	
	my_model = o
	string = request.POST['email_']
	my_model.email = string
	my_model.password = request.POST['pass_']
	my_model.name = request.POST['u_name']	
	my_model.save()
	#return render(request, 'signup/succesfull_signup.html')



def check_data(request):
	string = request.POST['email']
	password = request.POST['pass']
	try:
		o = User.objects.get(email=string, password=password)
		#o.user_set.all()
		return render(request, 'user/base.html',{'o': o})	
	except User.DoesNotExist:
		return render(request, 'user/user.html')
		
	my_model.save()
