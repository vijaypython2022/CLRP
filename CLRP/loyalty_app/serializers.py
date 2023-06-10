from rest_framework import serializers
from .models import Customer, LoyaltyTier


class LoyaltyTierSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoyaltyTier
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    tier = LoyaltyTierSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'
