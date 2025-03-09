from django.db import models
from django.contrib.auth.models import User


# ✔ Blockchain Tracking: Fields for transaction hash and block ID.
# ✔ Audit Fields: Better tracking for updates.
class Policy(models.Model):
    POLICY_TYPES = [
        ('basic', 'Basic'),
        ('premium', 'Premium'),
        ('vip', 'VIP'),
    ]
    
    PAYMENT_FREQUENCY = [
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('annually', 'Annually'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('canceled', 'Canceled'),
    ]

    policy_number = models.CharField(max_length=20, unique=True)
    policy_name = models.CharField(max_length=100)  
    description = models.TextField(blank=True, null=True)  
    policyholder = models.ForeignKey(User, on_delete=models.CASCADE)
    beneficiary_name = models.CharField(max_length=100, blank=True, null=True)
    beneficiary_relationship = models.CharField(max_length=50, blank=True, null=True)
    policy_type = models.CharField(max_length=10, choices=POLICY_TYPES)
    coverage_amount = models.DecimalField(max_digits=12, decimal_places=2)  # Increased precision
    premium_amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_frequency = models.CharField(max_length=10, choices=PAYMENT_FREQUENCY)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    # Blockchain fields
    blockchain_transaction_hash = models.CharField(max_length=100, blank=True, null=True, unique=True)
    block_id = models.CharField(max_length=100, blank=True, null=True)

    # Audit fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.policy_name} - {self.policyholder.username}"



 
# ✔ Hospital Relationship: Linked directly to hospitals.
# ✔ Blockchain Tracking: Claims stored on-chain for transparency.
# ✔ Claim Status Extended: Added 'Paid' status for claims that are reimbursed.
class Claim(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('paid', 'Paid'),
    ]

    claim_number = models.CharField(max_length=20, unique=True)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    description = models.TextField()
    claim_amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    
    hospital = models.ForeignKey("Hospital", on_delete=models.SET_NULL, blank=True, null=True)
    treatment_date = models.DateField(blank=True, null=True)
    doctor_report = models.FileField(upload_to='doctor_reports/', blank=True, null=True)
    policyholder_comments = models.TextField(blank=True, null=True)
    
    reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="reviewed_claims")
    reviewed_at = models.DateTimeField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    # Blockchain fields
    blockchain_transaction_hash = models.CharField(max_length=100, blank=True, null=True, unique=True)
    block_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Claim {self.claim_number} - {self.status}"


# ✔ Mpesa & Bank Tracking: Essential for Kenyan users.
# ✔ Blockchain Integration: For transparent payment validation
class Payment(models.Model):
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=[
        ('mpesa', 'Mpesa'),
        ('card', 'Credit/Debit Card'),
        ('bank', 'Bank Transfer'),
    ])
    transaction_id = models.CharField(max_length=50, unique=True)

    # Blockchain Tracking
    blockchain_transaction_hash = models.CharField(max_length=100, blank=True, null=True, unique=True)
    block_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Payment {self.transaction_id} - {self.amount}"

    

# Accreditation Number: Verifies hospitals.
# Insurance Policies Accepted: Better hospital-policy linkage.
class Hospital(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    is_partnered = models.BooleanField(default=True)
    accreditation_number = models.CharField(max_length=50, unique=True)  # New field
    insurance_accepted = models.ManyToManyField(Policy, blank=True)  # Link to policies

    def __str__(self):
        return self.name

    

# Multiple Policies per Holder: One user can have several policies.
class PolicyHolderProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField()
    national_id = models.CharField(max_length=20, unique=True)
    insurance_policies = models.ManyToManyField(Policy, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.national_id}"

    


# Tracks who made what changes & when (useful for disputes).
class PolicyAuditLog(models.Model):
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    change_description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Change on {self.policy.policy_number} by {self.changed_by.username}"


# Tracks claim payouts separately from payments.
class Reimbursement(models.Model):
    claim = models.OneToOneField(Claim, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=[
        ('mpesa', 'Mpesa'),
        ('bank', 'Bank Transfer'),
    ])
    transaction_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Reimbursement for {self.claim.claim_number} - {self.amount_paid}"

    
