import datetime

from _decimal import Decimal
from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Membership_tiers(models.Model):
    TIER_CHOICES = (
        ('silver', 'Silver'),
        ('gold', 'Gold'),
        ('platinum', 'Platinum'),
    )
    tier = models.CharField(max_length=10, choices=TIER_CHOICES, primary_key=True)
    requirement = models.CharField(max_length=100)
    discount = models.IntegerField()
    benifits = models.CharField(max_length=100)

    # tier_id = models.CharField(max_length=10, choices=TIER_CHOICES, unique=True)

    def __str__(self):
        return self.tier


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    address = models.CharField(max_length=150)
    membership = models.ForeignKey(Membership_tiers, on_delete=models.CASCADE)

    def is_eligible_for_reward(self):
        point = RewardPoints.objects.get(user=self.user)
        if point.points >= 100:
            return True
        else:
            return False

    def __str__(self):
        return self.name


class Vendor(models.Model):
    vid = models.IntegerField(primary_key=True, auto_created=True, blank=False, null=False)
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    desc = models.CharField(max_length=150)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    # Add any additional fields related to the product
    def save(self, *args, **kwargs):
        if not self.product_id:
            last_product = Product.objects.order_by('-id').first()
            if last_product:
                last_id = int(last_product.product_id[1:])  # Extract the number from the ID
                new_id = last_id + 1
            else:
                new_id = 1
            self.product_id = 'P{:03d}'.format(new_id)  # Format the ID with leading zeros if necessary
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class LoyaltyProgram(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    membership_tier = models.ForeignKey(Membership_tiers, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class RewardPoints(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateField(default=datetime.date.today() + datetime.timedelta(days=90))

    def __str__(self):
        return f"{self.customer.name} - {self.points}"


class Customer_purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    purchase_date = models.DateField(auto_now_add=True)
    loyaltyProgram = models.ForeignKey(LoyaltyProgram, on_delete=models.CASCADE)
    expiry_date = models.DateField(default=datetime.date.today() + datetime.timedelta(days=90))

    def __str__(self):
        return f"{self.customer.name} - {self.product.name}"

    def total_price(self):
        price = self.quantity * self.product.price
        # gst = price * 0.18  # Calculate 18% GST
        gst = price * Decimal('0.18')  # Convert 0.18 to Decimal
        total_price_with_gst = price + gst
        return total_price_with_gst

    total_price.short_description = 'Total Price'

    def is_eligible_for_reward(self):
        price = self.quantity * self.product.price
        if price >= 4000:
            return True
        else:
            return False


class RedemptionRequest(models.Model):
    RETURNED = 'Returned'
    PENDING = 'Pending'
    STATUS_CHOICES = [
        (RETURNED, 'Returned'),
        (PENDING, 'Pending'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    returned_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)

    # Other fields you may need
    # ...

    def __str__(self):
        return f'Redemption Request #{self.pk}'


class PurchaseReturn(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    return_quantity = models.PositiveIntegerField()
    return_reason = models.CharField(max_length=100)
    return_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Purchase Return ID: {self.id}"
