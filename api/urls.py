# from django.urls import path
# from .views import RegiserUserView,LoginView,PolicyListCreateView,ClaimDetailView,ClaimListCreateView


# urlpatterns  = [
#     path('register/',RegiserUserView.as_view(),name='register'),
#     path('login/',LoginView.as_view(),name='login'),
#     path('policies/',PolicyListCreateView.as_view(),name='policy-list-create'),
#     path('claims/',ClaimListCreateView.as_view(),name='claim-list-create'),
#     path('claims/<int:pk>/',ClaimDetailView.as_view(),name='claim-detail')
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PolicyViewSet, ClaimViewSet, PaymentViewSet, HospitalViewSet, 
    PolicyHolderProfileViewSet, PolicyAuditLogViewSet, ReimbursementViewSet
)

router = DefaultRouter()
router.register(r'policies', PolicyViewSet)
router.register(r'claims', ClaimViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'hospitals', HospitalViewSet)
router.register(r'policyholders', PolicyHolderProfileViewSet)
router.register(r'policy-audit-logs', PolicyAuditLogViewSet)
router.register(r'reimbursements', ReimbursementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
