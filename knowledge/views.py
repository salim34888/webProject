from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, ArticleCategory, UserFavorite


@login_required
def toggle_favorite(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    favorite, created = UserFavorite.objects.get_or_create(
        user=request.user,
        article=article
    )

    if not created:
        favorite.delete()
        messages.success(request, "Удалено из избранного")
    else:
        messages.success(request, "Добавлено в избранное")

    return redirect('article_detail', article_id=article_id)


@login_required
def article_list(request):
    categories = ArticleCategory.objects.all()
    selected_category = request.GET.get('category')
    search_query = request.GET.get('search')

    articles = Article.objects.all()

    if selected_category:
        articles = articles.filter(category__id=selected_category)

    if search_query:
        articles = articles.filter(title__icontains=search_query)

    return render(request, 'knowledge/list.html', {
        'articles': articles,
        'categories': categories
    })


@login_required
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    # Проверка PRO-доступа
    if article.is_pro and not request.user.pro_status == 'pro':
        return render(request, 'knowledge/pro_required.html')

    is_favorite = UserFavorite.objects.filter(
        user=request.user,
        article=article
    ).exists()

    return render(request, 'knowledge/detail.html', {
        'article': article,
        'is_favorite': is_favorite
    })