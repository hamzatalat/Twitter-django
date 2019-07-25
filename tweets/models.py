from django.db import models

from user_authentication.models import User

	
class Tweets(models.Model):
	tweeted_by = models.ForeignKey(User, on_delete=models.CASCADE)
	tweet = models.CharField(max_length=200)

class likes(models.Model):
	tweet = models.ForeignKey(Tweets, on_delete=models.CASCADE)
	liked_by = models.ForeignKey(User, on_delete=models.CASCADE)

class comments (models.Model):
	tweet = models.ForeignKey(Tweets, on_delete=models.CASCADE)
	commented_by = models.ForeignKey(User, on_delete=models.CASCADE)	
	comment  = models.CharField(max_length=200)
	


class follow (models.Model):
	user = models.ForeignKey(User, null=True, related_name='followers', on_delete=models.CASCADE)
	followed_by = models.ForeignKey(User, null=True, related_name='followed' ,on_delete=models.CASCADE)


