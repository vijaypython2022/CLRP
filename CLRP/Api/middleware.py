import datetime
from django.shortcuts import redirect
from .models import Customer, RedemptionRequest

# this middleware check the redeem request is eligible for the reward or not base on available point.
# if eligible send the session value True on end user UI.


class LoyaltyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            customer = Customer.objects.get(user=request.user)
            request.session['reward_eligible'] = False

            if customer.is_eligible_for_reward():
                last_returned_product = RedemptionRequest.objects.filter(
                    customer=customer,
                    status=RedemptionRequest.RETURNED
                ).order_by('-returned_date').first()

                if not last_returned_product:
                    request.session['reward_eligible'] = True
                elif last_returned_product.returned_date + datetime.timedelta(days=7) < datetime.datetime.now().date():
                    request.session['reward_eligible'] = True

        return response

    def process_view(self, request):
        return None
