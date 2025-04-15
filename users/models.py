from email.policy import default

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


class UserActivity(models.Model):
    ACTIVITY_TYPES = [
        ('test', 'Тестирование'),
        ('article', 'Чтение статьи'),
        ('goal', 'Прогресс цели')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    content_id = models.IntegerField()  # ID теста/статьи/цели
    content_title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)