from django.contrib import admin
from .models import Category, Orders, Rate, product

admin.site.register(Category)
admin.site.register(product)
admin.site.register(Rate)
admin.site.register(Orders)
