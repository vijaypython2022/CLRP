from _decimal import Decimal
from django.contrib import admin
from .models import Customer, Product, LoyaltyProgram, Customer_purchase, RewardPoints,\
    Membership_tiers, Vendor,RedemptionRequest,PurchaseReturn

# Register your models here.

admin.site.register(LoyaltyProgram)
admin.site.register(Membership_tiers)
admin.site.register(Vendor)
admin.site.register(RedemptionRequest)
admin.site.register(PurchaseReturn)


@admin.register(RewardPoints)
class RewardPointAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'points', 'last_updated','expiry_date']


@admin.register(Customer_purchase)
class Customer_purchaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'product', 'quantity','purchase_date','total_price','loyaltyProgram','expiry_date']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'mobile','address','membership']


@admin.register(Product)
class ProducttAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'name', 'price','desc','vendor']



