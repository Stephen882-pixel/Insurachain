from rest_framework import generics,permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .models import Claim,Policy
from .serializers import UserSerializer,PolicySerializer,ClaimSerializer


# Use Registration view

class RegiserUserView(APIView):
    def post(self,request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({'message':'username has alredy been taken'},status=400)
        
        user = User.objects.create_user(username=username,email=email,password=password)
        return Response({'message':'User registererd successfully'})
    

# JWT Token View (Login)
class LoginView(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh':str(refresh),
                'access':str(refresh.access_token)
            })
        return Response({'message':'Invalid credentials'},status=400)
    
# CRUD Views for policies and claims
class PolicyListCreateView(generics.ListCreateAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    permission_classes  = [permissions.IsAuthenticated]

class ClaimListCreateView(generics.ListCreateAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClaimDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
    permission_classes = [permissions.IsAuthenticated]
    