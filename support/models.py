from django.db import models
from users.models import User
from django.utils import timezone

class FAQCategory(models.Model):
    name = models.CharField("Категория", max_length=100)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Категория FAQ"
        verbose_name_plural = "Категории FAQ"
        ordering = ['order']

    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.CharField("Вопрос", max_length=255)
    answer = models.TextField("Ответ")
    category = models.ForeignKey(FAQCategory, on_delete=models.CASCADE, verbose_name="Категория")
    order = models.PositiveIntegerField("Порядок", default=0)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQ"
        ordering = ['category__order', 'order']

    def __str__(self):
        return self.question

class SupportTicket(models.Model):
    STATUS_CHOICES = [
        ('open', 'Открыт'),
        ('in_progress', 'В обработке'),
        ('resolved', 'Решен'),
        ('closed', 'Закрыт')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    subject = models.CharField("Тема", max_length=200)
    message = models.TextField("Сообщение")
    status = models.CharField(
        "Статус",
        max_length=20,
        choices=STATUS_CHOICES,
        default='open'
    )
    admin_response = models.TextField("Ответ администратора", blank=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Тикет поддержки"
        verbose_name_plural = "Тикеты поддержки"
        ordering = ['-created_at']

    def __str__(self):
        return f"Тикет #{self.id} - {self.subject}"

    def save(self, *args, **kwargs):
        if self.status in ['resolved', 'closed'] and not self.admin_response:
            raise ValueError("Для закрытия тикета необходим ответ администратора")
        super().save(*args, **kwargs)