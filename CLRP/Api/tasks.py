import datetime
from datetime import timedelta
from django.utils import timezone
from .models import Customer, RewardPoints
from celery import shared_task
from datetime import date


# This share task check every day for customer reward point expiry.if expired point get zero.

@shared_task
def expire_reward_points_task():
    today = date.today()
    expired = RewardPoints.objects.filter(expiry_date__lt=today)
    if expired.exists():
        for reward in expired:
            reward.points = 0
            reward.save()
    else:
        print('No objects found for expiry')

# @shared_task
# def update_reward_points(customer_id):
#     customer = Customer.objects.get(id=customer_id)
#     total_purchase = customer['price'] * customer['quantity']
#     if total_purchase > 4000:
#         customer.reward_points += 100
#         reward_points = RewardPoints.objects.create(customer=customer, points=100,
#                                                     last_updated=datetime.datetime.now())
#
#         reward_points.save()
#         update_expiry.apply_async(args=(customer_id,), eta=timezone.now() + timedelta(days=30))

# Run below beat schedular seperately for schedule task
# celery -A CLRP beat --loglevel=info

# Run task by calling any views or function when needed.
# celery -A CLRP worker --loglevel=info
