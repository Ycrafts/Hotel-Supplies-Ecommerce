from django.db import models
from apps.accounts.models import SupplierProfile

class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name

    
class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(unique=True, max_length=255) #unique identifier for the product filled out by the supplier
    description = models.TextField(max_length=512)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)
    img = models.ImageField(upload_to="product_images")
    supplier = models.ForeignKey(SupplierProfile, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    
class ProductInventory(models.Model):
    INVENTORY_UNITS = (
        ('kg', 'Kilogram'),
        ('pcs', 'Pieces'),
        ('ltr', 'Liter'),
        ('m', 'Meter'),
    )
    
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    stock_quantity = models.IntegerField(default=0) #the total amount of that product in the supplier's hands
    unit = models.CharField(max_length=10, choices=INVENTORY_UNITS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.stock_quantity} {self.unit} of {self.product.name}"
    