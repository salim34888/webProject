from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .models import FAQ, FAQCategory, SupportTicket
from .forms import SupportTicketForm


@login_required
def faq_list(request):
    categories = FAQCategory.objects.prefetch_related('faq_set').all()
    return render(request, 'support/faq_list.html', {
        'categories': categories
    })


@login_required
def ticket_list(request):
    tickets = SupportTicket.objects.filter(user=request.user).order_by('-created_at')

    paginator = Paginator(tickets, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'support/ticket_list.html', {
        'page_obj': page_obj
    })


@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = SupportTicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user  # Привязываем к текущему пользователю
            ticket.save()
            messages.success(request, 'Ваш запрос успешно отправлен!')
            return redirect('support:ticket_detail', ticket_id=ticket.id)
    else:
        form = SupportTicketForm()

    return render(request, 'support/create_ticket.html', {'form': form})

@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(SupportTicket, id=ticket_id, user=request.user)
    return render(request, 'support/ticket_detail.html', {
        'ticket': ticket
    })