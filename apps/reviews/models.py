from django.db import models
from apps.accounts.models import BuyerProfile
from django.core.validators import MinValueValidator, MaxValueValidator

class ProductReview(models.Model):
    buyer = models.ForeignKey(BuyerProfile, on_delete=models.CASCADE, related_name="product_reviews")
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    ) 
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.rating}/5 by {self.buyer.company_name}"


class SupplierReview(models.Model):
    buyer = models.ForeignKey(BuyerProfile, on_delete=models.CASCADE, related_name="supplier_reviews")
    supplier = models.ForeignKey('accounts.SupplierProfile', on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )  
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.supplier.company_name} - {self.rating}/5 by {self.buyer.company_name}"
