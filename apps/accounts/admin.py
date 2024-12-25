from django.contrib import admin
from .models import CustomUser, Address, SupplierProfile, BuyerProfile
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "email",
        "is_staff",
        "role",
    ]
    add_fieldsets = (
        (None,{"classes": ("wide",),"fields": ("username","email","password1", "password2","role"),},),
    )
    fieldsets = (
        (None,{"classes": ("wide",),"fields": ("username","email","password","role"),},),
    )
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(BuyerProfile)
admin.site.register(SupplierProfile)
admin.site.register(Address)
    
    
