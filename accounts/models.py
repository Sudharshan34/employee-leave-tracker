from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('employee', 'Employee'),
        ('manager', 'Manager'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')
    sick_leave_balance = models.IntegerField(default=12)
    casual_leave_balance = models.IntegerField(default=10)
    earned_leave_balance = models.IntegerField(default=15)

    def __str__(self):
        return f"{self.username} ({self.role})"