from django.urls import path
from .views import test_list, take_test

urlpatterns = [
    path('', test_list, name='test_list'),
    path('<int:test_id>/', take_test, name='take_test'),
    path('<int:test_id>/result/', take_test, name='test_result'),  # Для примера
]