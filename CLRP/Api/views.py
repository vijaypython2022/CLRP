from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Customer, Customer_purchase, RewardPoints
from .serializers import RewardPointsSerializer, Customer_purchaseSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from datetime import datetime, timedelta
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from .tasks import expire_reward_points_task
from django.http import HttpResponse
from datetime import date
from django.views.generic import DetailView,TemplateView


# call the celery task using function

class CustomerAccount(TemplateView):
    model = Customer
    context_object_name = 'login'
    template_name = 'customer/customer_login.html'


def test_celery(request):
    # expire_reward_points_task.delay()
    expire_reward_points_task.delay()
    return HttpResponse('Done')


# test func
def check_expiry_point(request):
    today = date.today()
    expired = RewardPoints.objects.filter(expiry_date__lte=today)
    if expired.exists():
        for reward in expired:
            reward.points = 0
            reward.save()
    else:
        print('No objects found for expiry')
    return HttpResponse('Expiry check Done!')


class CustomerPurchaseViewSet(viewsets.ModelViewSet):
    queryset = Customer_purchase.objects.all()
    serializer_class = Customer_purchaseSerializer
    authentication_classes = [JWTAuthentication]
    # authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #
    #     # Check if the purchase amount is greater than or equal to 4000
    #     purchase_amount = serializer.validated_data['quantity'] * serializer.validated_data['product'].price
    #     if purchase_amount >= 4000:
    #         customer = serializer.validated_data['customer']
    #         purchase_date = serializer.validated_data['purchase_date']
    #         # Add 100 reward points after 7 days from the purchase date
    #         reward_points_expiry = purchase_date + timedelta(minutes=2)
    #         reward_points = RewardPoints.objects.create(customer=customer, points=100,
    #                                                     last_updated=reward_points_expiry)
    #
    #         # Save the reward points
    #         reward_points.save()

    # headers = self.get_success_headers(serializer.data)
    # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class RewardPointsViewSet(viewsets.ModelViewSet):
    queryset = RewardPoints.objects.all()
    serializer_class = RewardPointsSerializer

# @api_view(['POST'])
# def purchase_update(request):
#     customer_id = request.data.get(
#         'customer_id')  # Assuming you pass the user_id and purchase_amount in the request# data
#     total_price = request.data.get('total_price')
#
#     if customer_id is None or total_price is None:
#         return Response({'error': 'user_id and purchase_amount are required fields'}, status=400)
#
#     try:
#         customer = Customer.objects.get(id=customer_id)
#     except Customer.DoesNotExist:
#         return Response({'error': 'Invalid user_id'}, status=400)
#
#     try:
#         reward_point = RewardPoints.objects.get(customer=customer)
#     except RewardPoints.DoesNotExist:
#         reward_point = RewardPoints.objects.create(customer=customer)
#
#     if total_price >= 4000:
#         reward_point.points += 100
#         reward_point.save()
#
#     serializer = RewardPointsSerializer(reward_point)
#     return Response(serializer.data)
