from django.contrib import admin
from users.models import MyUser


class User_list(admin.ModelAdmin):
    pass
admin.site.register(MyUser, User_list)