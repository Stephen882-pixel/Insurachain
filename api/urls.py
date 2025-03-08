from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PolicyViewSet,ClaimViewSet,PaymentViewSet,AuditLogViewSet

router = DefaultRouter()
router.register(r'policies',PolicyViewSet)
router.register(r'claims',ClaimViewSet)
router.register(r'payments',PaymentViewSet)
router.register(r'audits',AuditLogViewSet)

urlpatterns = [
    path('',include(router.urls))
]

