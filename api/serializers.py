from rest_framework import serializers
from .models import Policy, Claim, Payment, Hospital, PolicyHolderProfile, PolicyAuditLog, Reimbursement

class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = '__all__'

class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

class PolicyHolderProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyHolderProfile
        fields = '__all__'

class PolicyAuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyAuditLog
        fields = '__all__'

class ReimbursementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reimbursement
        fields = '__all__'
