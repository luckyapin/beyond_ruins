from django.contrib import admin

from .models import *
# Register your models here.

# Регистрация моделей в админ-панели
admin.site.register(Categories)
admin.site.register(Posts)
admin.site.register(Comments)