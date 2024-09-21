from django.contrib import admin

from .models import Product, Embedding
# Register your models here.

admin.site.register(Product)

admin.site.register(Embedding)