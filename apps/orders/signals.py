from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderItem

@receiver(post_save, sender=OrderItem)
def update_order_total_on_save(sender, instance, **kwargs):
    #Update the order's total_price whenever an OrderItem is saved.
    
    instance.order.update_total_price()

@receiver(post_delete, sender=OrderItem)
def update_order_total_on_delete(sender, instance, **kwargs):
    #Update the order's total_price whenever an OrderItem is deleted.

    instance.order.update_total_price()
