from .models import Customer_purchase, RewardPoints
from django.db.models.signals import post_save
from django.dispatch import receiver


# This Signal is trigger when customer purchase 4000 or more product.and give the reward point
# customer account.

@receiver(post_save, sender=Customer_purchase)
def handle_customer_purchase(sender, instance, created, **kwargs):
    if created:
        reward = instance.is_eligible_for_reward()
        print('reward value:', reward)
        if reward:
            # Calculate reward points based on the purchase amount
            purchase_amount = instance.total_price()
            reward_points = purchase_amount // 100  # 1 points per Rs. 100 spent
            print('Signal Trigger')
            # Get or create the RewardPoints object for the customer
            reward_points_obj, _ = RewardPoints.objects.get_or_create(customer=instance.customer)

            # Update the reward points and save the object
            reward_points_obj.points += reward_points
            reward_points_obj.save()
        else:
            print('Customer not eligible for reward point')


def handle_customer_product_return(sender, instance, created, **kwargs):
    '''this signal trigger when the customer return product and perform reward point related operation
    like point deduct from the customer account.
    '''
    pass
