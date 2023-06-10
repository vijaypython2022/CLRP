from _decimal import Decimal
from django.contrib import admin
from .models import Customer, Product, LoyaltyProgram, Customer_purchase, RewardPoints, Membership_tiers, Vendor

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(LoyaltyProgram)
admin.site.register(Membership_tiers)
admin.site.register(Vendor)


@admin.register(RewardPoints)
class RewardPointAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'points', 'last_updated']


@admin.register(Customer_purchase)
class RewardPointAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'product', 'quantity','purchase_date','total_price','loyaltyProgram','expiry_date']

