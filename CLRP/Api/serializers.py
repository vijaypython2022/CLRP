from rest_framework import serializers
from .models import Customer, Product, LoyaltyProgram, Customer_purchase, RewardPoints, Membership_tiers, Vendor


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class LoyaltyProgrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoyaltyProgram
        fields = '__all__'


class Customer_purchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_purchase
        fields = '__all__'


class RewardPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardPoints
        fields = '__all__'


class Membership_tiersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership_tiers
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
