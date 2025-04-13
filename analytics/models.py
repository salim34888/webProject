from django.db import models
from users.models import User

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    tests_completed = models.PositiveIntegerField(default=0)
    skills_improvement = models.JSONField(default=dict)
