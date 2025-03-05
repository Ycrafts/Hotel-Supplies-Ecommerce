from rest_framework import serializers
from .models import Product, ProductCategory, ProductInventory, Unit

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ["id", "name", "description"]    

class UnitSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ["__all__"]

class ProductSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["__all__"]

class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventory
        fields = [""]

