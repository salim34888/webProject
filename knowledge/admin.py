from django.contrib import admin
from .models import ArticleCategory, Article

@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_pro')
    search_fields = ('title', 'content')
    list_filter = ('category', 'is_pro')