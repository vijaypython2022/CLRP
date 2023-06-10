# tasks.py
import datetime
from datetime import timedelta
from celery import shared_task
from django.utils import timezone
from .models import Customer, RewardPoints


@shared_task
def update_reward_points(customer_id):
    customer = Customer.objects.get(id=customer_id)
    total_purchase = customer['price'] * customer['quantity']
    if total_purchase > 4000:
        customer.reward_points += 100
        reward_points = RewardPoints.objects.create(customer=customer, points=100,
                                                    last_updated=datetime.datetime.now())

        reward_points.save()
        update_expiry.apply_async(args=(customer_id,), eta=timezone.now() + timedelta(days=30))


@shared_task
def update_expiry(customer_id):
    customer = Customer.objects.get(id=customer_id)
    customer.reward_points -= 100
    customer.save()
