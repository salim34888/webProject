from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('report/', views.generate_pdf_report, name='pdf_report'),

]