from django.contrib import admin

from .models import Product, ProductCategory, ProductInventory, Unit

admin.site.register(ProductInventory)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Unit)

