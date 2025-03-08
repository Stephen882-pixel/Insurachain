from rest_framework import viewsets,permissions
from rest_framework.response import Response
from .models import User,Payment,Policy,Auditlog,Claim
from .serializers import UserSerializer,PaymentSerializer,PolicySerializer,AuditLogSerializer,ClaimSerializer




# Nested serializer for the user model

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
        claim = serializer.save(user=self.request.user)  # Save the claim with the logged-in user

        print(f"Logging action for user:",self.request.user)
        print(f"Claim ID:",claim.id)

        log = Auditlog.objects.create(
            user=self.request.user,
            action="Submitted a new claim",
            details=f"Claim ID: {claim.id} for Policy ID: {claim.policy.id}, Amount: {claim.amount_requested}"
        )

        print("Audit log created:", log)


    
# Payment viewwset
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


# Audit log viewset
class AuditLogViewSet(viewsets.ModelViewSet):
    queryset = Auditlog.objects.all()
    serializer_class = AuditLogSerializer
    permission_classes = [permissions.IsAdminUser]


    def list(self,request,*args,**kwargs):
        logs = Auditlog.objects.all()
        if not logs.exists():
            return Response({
                "message":"No audit logs found."
            },status=200)
        return super().list(request,*args,**kwargs)
    
    
