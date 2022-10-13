from django.contrib import admin

# Register your models here.
from .models import Product, OrderDetail

admin.site.register(Product)
admin.site.register(OrderDetail)
