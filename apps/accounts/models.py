from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    ROLES = (
        ("supplier", "Supplier"),
        ("buyer", "Buyer"),
    )
    
    role = models.CharField(max_length=10, choices=ROLES)
    def __str__(self):
        return f"{self.username} {self.role}"
    
    @property
    def is_consumer(self):
        return self.role == "buyer"
    
    @property
    def is_supplier(self):
        return self.role == "supplier"
    
class Address(models.Model):
    city = models.CharField(max_length=100)
    kebele = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.city} {self.kebele}"

class SupplierProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="supplier_profile")
    company_name = models.CharField(max_length=255)
    work_place_address = models.ManyToManyField(Address, related_name="suppliers")
    business_license = models.FileField(upload_to="licenses/")
    
    def __str__(self):
        return self.company_name
    
class BuyerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name = "buyer_profile")
    company_name = models.CharField(max_length=255)
    address = models.ManyToManyField(Address, related_name="buyers")
    
    def __str__(self):
        return self.company_name
    