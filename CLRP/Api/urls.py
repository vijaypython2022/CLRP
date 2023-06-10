from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerPurchaseViewSet,RewardPointsViewSet\

router = DefaultRouter()
router.register(r'sales-masters', CustomerPurchaseViewSet)
router.register(r'reward-points', RewardPointsViewSet)

urlpatterns = [
    path('1', include(router.urls)),
]
