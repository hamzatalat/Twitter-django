from django.urls import path

from . import views

app_name = 'tweets'
urlpatterns = [
	path('home/<int:ids>', views.Home, name='home'),
	path('posttweet/<int:ids>', views.posttweet, name='posttweet'),
	path('savetweet/<int:ids>', views.savetweet, name='savetweet'),
	path('finduser/<int:ids>', views.finduser, name='finduser'),
	path('fonduser/<int:ids>', views.fonduser, name='fonduser'),
	path('followuser/<int:ids>/<int:aids>', views.followuser, name='followuser'),
	path('viewtweets/<int:ids>', views.viewtweets, name='viewtweets'),
	path('liketweet/<int:ids>/<str:aids>', views.liketweet, name='liketweet'),
	path('commenttweet/<int:ids>/<str:aids>', views.commenttweet, name='commenttweet'),

]
