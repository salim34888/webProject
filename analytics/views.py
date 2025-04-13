from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import UserGoal
from tests.models import TestResult
from django.db import models


@login_required
def dashboard(request):
    # Статистика по целям
    goals = UserGoal.objects.filter(user=request.user)
    goals_data = {
        'completed': goals.filter(progress=100).count(),
        'in_progress': goals.exclude(progress=100).count()
    }

    # Статистика по тестам
    test_results = TestResult.objects.filter(user=request.user)
    test_stats = {
        'total_tests': test_results.count(),
        'avg_score': test_results.aggregate(models.Avg('score'))['score__avg'] or 0
    }

    return render(request, 'analytics/dashboard.html', {
        'goals_data': goals_data,
        'test_stats': test_stats
    })