from django.contrib import admin

# Register your models here.
from .models import Product, Quote

admin.site.register(Product)
admin.site.register(Quote)