from django.db import models
from django.forms import ValidationError
from apps.accounts.models import BuyerProfile
from apps.products.models import Product, Unit
from decimal import Decimal
from django.db import transaction

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    
    buyer = models.ForeignKey(BuyerProfile, on_delete=models.CASCADE, related_name="orders")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def update_total_price(self):
        with transaction.atomic():  # to roll back incase an item is created but the total price is left unupdated
            self.refresh_from_db()
            # Dynamically calculate the total price from related OrderItems
            self.total_price = sum(
                (item.quantity * item.price_per_unit).quantize(Decimal("0.01")) for item in self.items.all()
            )
            self.save()
    def __str__(self):
        return f"Order #{self.id} by {self.buyer.company_name} - {self.status} for {self.total_price}"


class OrderItem(models.Model):

    PLATFORM_SHARE_PERCENTAGE = Decimal("0.1")  # Defined as a class-level constant

    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)  # quantity is always positive
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    platform_share = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  
    supplier_earnings = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  

   
    def save(self, *args, **kwargs):
        if self.quantity <= 0:
                raise ValidationError("Quantity must be greater than zero.")
        if self.price_per_unit < 0:
                raise ValidationError("Price per unit cannot be negative.")

         # calculations for finding supplier and platform share
        subtotal = Decimal(self.price_per_unit) * Decimal(self.quantity)
        self.platform_share = (subtotal * self.PLATFORM_SHARE_PERCENTAGE).quantize(Decimal("0.01"))
        self.supplier_earnings = (subtotal - self.platform_share).quantize(Decimal("0.01"))
        
        super().save(*args, **kwargs)                       
            
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)  
            
            
    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Order #{self.order.id})"
        
