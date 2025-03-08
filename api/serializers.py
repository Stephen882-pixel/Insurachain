from rest_framework import serializers
from .models import User,Policy,Claim,Payment,Auditlog
from django.contrib.auth import get_user_model

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id','username','email','role']

# Policy serializer
class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = '__all__'

# Claim serializer
class ClaimSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Claim
        fields = '__al__'

# Payment Serializer
class PaymentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = '__all__'

# Audit log serializer
class AuditLogSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Auditlog
        fields = '__all__'

        