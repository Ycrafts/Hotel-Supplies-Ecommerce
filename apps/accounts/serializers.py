from rest_framework import serializers

from .models import (
    CustomUser, BuyerProfile, SupplierProfile, Address
)

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class SupplierProfileSerializer(serializers.ModelSerializer):
    # Nested serializer to handle work_place_address details
    work_place_address = AddressSerializer(many=True)

    class Meta:
        model = SupplierProfile
        fields = "__all__"
        read_only_fields = ['user']

    def create(self, validated_data):
        # Extract work_place_address data
        addresses_data = validated_data.pop('work_place_address', [])
        supplier = SupplierProfile.objects.create(**validated_data)
        for address_data in addresses_data:
            address, _ = Address.objects.get_or_create(**address_data)
            supplier.work_place_address.add(address)
        return supplier

    def update(self, instance, validated_data):
        # Extract work_place_address data
        addresses_data = validated_data.pop('work_place_address', [])
        # Update other fields
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.save()

        # Update addresses
        instance.work_place_address.clear()
        for address_data in addresses_data:
            address, _ = Address.objects.get_or_create(**address_data)
            instance.work_place_address.add(address)
        return instance


class BuyerProfileSerializer(serializers.ModelSerializer):
    # Nested serializer to handle address details
    address = AddressSerializer(many=True)

    class Meta:
        model = BuyerProfile
        fields = "__all__"

    def create(self, validated_data):
        # Extract address data
        addresses_data = validated_data.pop('address', [])
        buyer = BuyerProfile.objects.create(**validated_data)
        for address_data in addresses_data:
            address, _ = Address.objects.get_or_create(**address_data)
            buyer.address.add(address)
        return buyer

    def update(self, instance, validated_data):
        # Extract address data
        addresses_data = validated_data.pop('address', [])
        # Update other fields
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.save()

        # Update addresses
        instance.address.clear()
        for address_data in addresses_data:
            address, _ = Address.objects.get_or_create(**address_data)
            instance.address.add(address)
        return instance


class CustomUserSerializer(serializers.ModelSerializer):
    # Include nested serializers for profiles
    supplier_profile = SupplierProfileSerializer(read_only=True)
    buyer_profile = BuyerProfileSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'email', 'role',
            'supplier_profile', 'buyer_profile'
        ]

    def to_representation(self, instance):
    
        # Customize the representation to include only the profile relevant to the user's role.
       
        data = super().to_representation(instance)
        if instance.role == 'buyer':
            data.pop('supplier_profile', None)
        elif instance.role == 'supplier':
            data.pop('buyer_profile', None)
        return data
