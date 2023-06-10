from django.contrib import admin
from .models import Customer,LoyaltyTier
# Register your models here.


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'tier','reward_points','total_purchases']


@admin.register(LoyaltyTier)
class LoyaltyTierAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'minimum_purchase']
