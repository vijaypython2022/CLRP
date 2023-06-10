import datetime

from _decimal import Decimal
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobile = models.IntegerField(max_length=10)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    vid = models.IntegerField(primary_key=True, auto_created=True, blank=False, null=False)
    name = models.CharField(max_length=100)
    mobile = models.IntegerField(max_length=10)
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


class Membership_tiers(models.Model):
    name = models.CharField(max_length=100)
    requirement = models.CharField(max_length=100)
    discount = models.IntegerField()
    benifits = models.CharField(max_length=100)

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
        price =self.quantity * self.product.price
        # gst = price * 0.18  # Calculate 18% GST
        gst = price * Decimal('0.18')  # Convert 0.18 to Decimal
        total_price_with_gst = price + gst
        return total_price_with_gst

    total_price.short_description = 'Total Price'