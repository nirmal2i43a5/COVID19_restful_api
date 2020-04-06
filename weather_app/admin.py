from django.contrib import admin

from .models import City

@admin.register(City)
class CityModel(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.


