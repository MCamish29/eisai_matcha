from django.contrib import admin
from .models import Category, Country, Tea, Equipment, Kit

# Register your models here.
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Tea)
admin.site.register(Equipment)
admin.site.register(Kit)
