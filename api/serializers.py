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
    user = serializers.PrimaryKeyRelatedField(read_only=True)  # Store user as ID
    date_submitted = serializers.DateTimeField(format='iso-8601',read_only=True)

    class Meta:
        model = Claim
        fields = ["id","user","policy", "amount_requested","status","date_submitted","remarks"]

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data['user'] = request.user # Associate the authenticated user
        return super().create(validated_data)
    


    
 
# Payment Serializer
class PaymentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = ['id','user','policy','amount','payment_type','transaction_id','status','timestamp']

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)

# Audit log serializer
class AuditLogSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Auditlog
        fields = '__all__'

