from django.contrib import admin
from .models import User
from django.contrib.auth.models import UserManager
# Register your models here.

admin.site.register(User,UserManager)