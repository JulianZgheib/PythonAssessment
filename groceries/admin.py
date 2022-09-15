from atexit import register
from django.contrib import admin
from groceries.models import Customers,Staff,Products
# Register your models here.

admin.site.register(Customers)
admin.site.register(Staff)
admin.site.register(Products)