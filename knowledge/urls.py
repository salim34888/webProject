from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('<int:article_id>/favorite/', views.toggle_favorite, name='toggle_favorite'),
]