from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerPurchaseViewSet,RewardPointsViewSet,test_celery,check_expiry_point,CustomerAccount

router = DefaultRouter()
router.register(r'purchase-masters', CustomerPurchaseViewSet)
router.register(r'reward-points', RewardPointsViewSet)

urlpatterns = [
    path('1', include(router.urls)),
    path('2', CustomerPurchaseViewSet.as_view({'create':'create'}),name='CPV'),
    path('call/',test_celery),
    path('test/',check_expiry_point),
    path('login/',CustomerAccount.as_view(),name='customer_login'),


]
