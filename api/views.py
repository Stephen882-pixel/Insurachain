# from rest_framework import generics,permissions
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth.models import User
# from .models import Claim,Policy
# from .serializers import UserSerializer,PolicySerializer,ClaimSerializer


from rest_framework import viewsets
from .models import Policy, Claim, Payment, Hospital, PolicyHolderProfile, PolicyAuditLog, Reimbursement
from .serializers import (
    PolicySerializer, ClaimSerializer, PaymentSerializer, 
    HospitalSerializer, PolicyHolderProfileSerializer, 
    PolicyAuditLogSerializer, ReimbursementSerializer
)


# Use Registration view

# class RegiserUserView(APIView):
#     def post(self,request):
#         username = request.data.get('username')
#         email = request.data.get('email')
#         password = request.data.get('password')

#         if User.objects.filter(username=username).exists():
#             return Response({'message':'username has alredy been taken'},status=400)
        
#         user = User.objects.create_user(username=username,email=email,password=password)
#         return Response({'message':'User registererd successfully'})
    

# # JWT Token View (Login)
# class LoginView(APIView):
#     def post(self,request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = User.objects.filter(username=username).first()

#         if user and user.check_password(password):
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'refresh':str(refresh),
#                 'access':str(refresh.access_token)
#             })
#         return Response({'message':'Invalid credentials'},status=400)
    
# CRUD Views for policies and claims

class PolicyViewSet(viewsets.ModelViewSet):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer

class ClaimViewSet(viewsets.ModelViewSet):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class PolicyHolderProfileViewSet(viewsets.ModelViewSet):
    queryset = PolicyHolderProfile.objects.all()
    serializer_class = PolicyHolderProfileSerializer

class PolicyAuditLogViewSet(viewsets.ModelViewSet):
    queryset = PolicyAuditLog.objects.all()
    serializer_class = PolicyAuditLogSerializer

class ReimbursementViewSet(viewsets.ModelViewSet):
    queryset = Reimbursement.objects.all()
    serializer_class = ReimbursementSerializer
