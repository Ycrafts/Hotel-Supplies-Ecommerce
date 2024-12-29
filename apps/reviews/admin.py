from django.contrib import admin
from .models import ProductReview, SupplierReview

admin.site.register(ProductReview)
admin.site.register(SupplierReview)