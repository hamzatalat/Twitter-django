from django.urls import path

from . import views

app_name = 'user_authentication'
urlpatterns = [
	path('', views.Base.as_view(), name='base'),
	path('signin', views.signin.as_view(), name='signin'),
	path('savedata', views.savedata, name='savedata'),
	path('check_data', views.check_data, name='check_data'),
	path('updatedata/<int:ids>', views.updatedata, name='updatedata'),
	path('ChangeProfile/<int:ids>', views.ChangeProfile, name='ChangeProfile'),
]
