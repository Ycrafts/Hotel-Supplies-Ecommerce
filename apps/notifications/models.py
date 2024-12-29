from django.db import models
from apps.accounts.models import CustomUser

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="notification")
    message = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Notificaiton for {self.user} : {'Read' if self.is_read else 'Unread'}"