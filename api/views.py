from rest_framework import viewsets,permissions
from rest_framework.response import Response
from .models import User,Payment,Policy,Auditlog,Claim
from .serializers import UserSerializer,PaymentSerializer,PolicySerializer,AuditLogSerializer,ClaimSerializer



# Policy viewset
class PolicyViewSet(viewsets.ModelViewSet):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    permission_classes = [permissions.IsAuthenticated]

# Claim viewset
class ClaimViewSet(viewsets.ModelViewSet):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
# Payment viewwset
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

# Audit log viewset
class AuditLogViewSet(viewsets.ModelViewSet):
    queryset = Auditlog.objects.all()
    serializer_class = AuditLogSerializer
    permission_classes = [permissions.IsAdminUser]
    
