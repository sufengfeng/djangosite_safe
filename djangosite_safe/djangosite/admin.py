from django.contrib import admin

# Register your models here.
from djangosite.models import Question, UserInfo

admin.site.register(Question)
admin.site.register(UserInfo)