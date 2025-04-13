from django.urls import path
from . import views

app_name = 'support'

urlpatterns = [
    path('faq/', views.faq_list, name='faq_list'),
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('tickets/new/', views.create_ticket, name='create_ticket'),
    path('tickets/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
]