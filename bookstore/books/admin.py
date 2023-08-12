# accounts/admin.py

from django.contrib import admin
from .models import UserLogin, FormRegister

admin.site.register(UserLogin)
admin.site.register(FormRegister)
