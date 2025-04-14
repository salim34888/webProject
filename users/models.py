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


class UserRanking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='ranking')
    total_score = models.IntegerField(default=0)
    tests_completed = models.IntegerField(default=0)
    last_activity = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-total_score', '-tests_completed']
        verbose_name = 'Рейтинг пользователя'
        verbose_name_plural = 'Рейтинги пользователей'

    def __str__(self):
        return f"{self.user.username} - {self.total_score} баллов"