from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Custom User model
class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='api_users',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='api_users_permissions',
        blank=True
    )
    ROLE_CHOICES = (
        ('admin','Admin'),
        ('insuarance_comapany','Insuarance Company'),
        ('policyholder','Policyholder'),
        ('agent','Agent'),
    )
    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default='policyholder')


# Insuarance policy model
class Policy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    premium_acccount = models.DecimalField(max_digits=10,decimal_places=2)
    coverage_details = models.TextField()
    terms_and_conditions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# Claims model
class Claim(models.Model):
    STATUS_CHOICES = (
        ('pending','Pending'),
        ('approved','Approved'),
        ('rejected','Rejected'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    policy = models.ForeignKey(Policy,on_delete=models.CASCADE)
    amount_requested = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending')
    date_submitted = models.DateTimeField(auto_now_add=True)
    remarks = models.TextField(blank=True,null=True)

    def __str__(self):
        return f"{self.user.username} - {self.policy.name} - {self.status}"
    
#Payment model
class Payment(models.Model):
    PAYMENT_TYPE_CHOICE = (
        ('premium','Premium'),
        ('claim_layout','Claim Payout')
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE,blank=True,null=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    payment_type = models.CharField(max_length=20,choices=PAYMENT_TYPE_CHOICE)
    transaction_id = models.CharField(max_length=100,unique=True)
    status = models.CharField(max_length=20,default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.payment_type} - {self.amount}"
    
# Audits Logs Model
class Auditlog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.action}"
    
