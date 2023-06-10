from rest_framework import viewsets
from .models import Customer, LoyaltyTier
from .serializers import CustomerSerializer, LoyaltyTierSerializer


class LoyaltyTierViewSet(viewsets.ModelViewSet):
    queryset = LoyaltyTier.objects.all()
    serializer_class = LoyaltyTierSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
