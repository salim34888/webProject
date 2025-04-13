from django.db import models
from users.models import User

class ArticleCategory(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE)
    is_pro = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=200, blank=True)

class UserFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)