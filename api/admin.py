from django.contrib import admin

from accounts.models import User
from posts.models import Posts

# Register your models here.
admin.site.register(User)
admin.site.register(Posts)