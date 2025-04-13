from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class User(AbstractUser):
    PRO_STATUS_CHOICES = [
        ('free', 'Free'),
        ('pro', 'Pro'),
    ]
    pro_status = models.CharField(
        max_length=10,
        choices=PRO_STATUS_CHOICES,
        default='free'
    )


class UserGoal(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    target_date = models.DateField()
    progress = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)