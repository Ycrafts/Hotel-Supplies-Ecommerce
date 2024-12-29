from django.db import models
from apps.orders.models import Order

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="payments")
    transaction_id = models.CharField(max_length=255, unique=True, blank=True, null=True)  # Allow null for initial creation with 
                                                                                            # no fields for cash on delivery
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('completed', 'Completed'),
            ('failed', 'Failed'),
        ],
        default="pending"
    )
    payment_method = models.CharField(
        max_length=20,
        choices=[
            ('cash_on_delivery', 'Cash on delivery'),
            ('stripe', 'Stripe'),
            ('telebirr', 'Telebirr'),
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # To track status updates

    def __str__(self):
        return f"Payment for Order #{self.order.id} - {self.payment_status}"

    def save(self, *args, **kwargs):
        # Auto-fill the amount from the related order, but allow manual override for flexibility
        if not self.amount and self.order:
            self.amount = self.order.total_price
        super().save(*args, **kwargs)
