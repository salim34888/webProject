from django.urls import path
from . import views

app_name = 'users'  # Это критически важно!

urlpatterns = [
    path('register/', views.SignUpView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('upgrade-pro/', views.upgrade_to_pro, name='upgrade_pro'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]