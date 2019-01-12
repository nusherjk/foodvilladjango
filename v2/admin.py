from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.FoodData)
admin.site.register(models.Complaints)
# Register your models here.
