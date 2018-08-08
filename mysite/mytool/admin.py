from django.contrib import admin

from .models import Password, Category

admin.site.register(Category)
admin.site.register(Password)
