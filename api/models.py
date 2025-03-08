from django.db import models
from django.contrib.auth.models import User


class Policy(models.Model):
    POLICY_TYPES = [
        ('basic','Basic'),
        ('premium','Premium'),
        ('vip','VIP'),
    ]
    policy_number = models.CharField(max_length=20,unique=True)
    policyholder =models.ForeignKey(User,on_delete=models.CASCADE)
    policy_type = models.CharField(max_length=10,choices=POLICY_TYPES)
    coverage_amount = models.DecimalField(max_digits=10,decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.policy_number} - {self.policyholder.username}"
    

class Claim(models.Model):
    STATUS_CHOICES = [
        ('pending','Pending'),
        ('approved','Approved'),
        ('rejected','Rejected'),
    ]
    claim_number = models.CharField(max_length=20,unique=True)
    policy = models.ForeignKey(Policy,on_delete=models.CASCADE)
    description = models.TextField()
    claim_amount = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Claim {self.claim_number} - {self.status}"


    
