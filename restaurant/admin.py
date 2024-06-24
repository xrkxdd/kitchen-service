from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import DishType, Cook, Dish


admin.site.register(DishType)
admin.site.register(Dish)
admin.site.register(Cook, UserAdmin)
