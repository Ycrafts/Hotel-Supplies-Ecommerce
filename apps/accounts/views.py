from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser, BuyerProfile, SupplierProfile, Address
from .serializers import CustomUserSerializer, BuyerProfileSerializer, AddressSerializer, SupplierProfileSerializer
from rest_framework.permissions import IsAdminUser

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]
    
class BuyerProfileViewSet(viewsets.ModelViewSet):
    queryset = BuyerProfile.objects.all()
    serializer_class = BuyerProfileSerializer

class SupplierProfileViewSet(viewsets.ModelViewSet):
    queryset = SupplierProfile.objects.all()
    
    