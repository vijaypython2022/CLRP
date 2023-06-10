from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoyaltyTierViewSet, CustomerViewSet

router = DefaultRouter()
router.register(r'loyalty-tiers', LoyaltyTierViewSet)
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('1', include(router.urls)),
]
