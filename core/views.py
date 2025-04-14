from django.shortcuts import render
from tests.models import Test
from knowledge.models import Article


def home(request):
    # Получаем 3 последних теста
    latest_tests = Test.objects.order_by('-id')[:3]

    # Получаем 3 популярные статьи (пример)
    popular_articles = Article.objects.order_by('-id')[:3]

    return render(request, 'core/home.html', {
        'latest_tests': latest_tests,
        'popular_articles': popular_articles,
    })