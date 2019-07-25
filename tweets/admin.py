from django.contrib import admin
from tweets.models import Tweets ,likes ,comments ,follow
# Register your models here.

admin.site.register(Tweets)
admin.site.register(likes)
admin.site.register(comments)
admin.site.register(follow)


