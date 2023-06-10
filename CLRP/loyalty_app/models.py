from django.db import models


class LoyaltyTier(models.Model):
    name = models.CharField(max_length=255)
    minimum_purchase = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    tier = models.ForeignKey(LoyaltyTier, on_delete=models.SET_NULL, null=True)
    reward_points = models.PositiveIntegerField(default=0)
    total_purchases = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name
