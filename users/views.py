from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm
from .models import User
from .models import UserRanking
from django.views.generic import CreateView, UpdateView


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        messages.success(self.request, 'Регистрация прошла успешно!')
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activities'] = self.request.user.useractivity_set.order_by('-created_at')[:10]
        return context


@login_required
def upgrade_to_pro(request):
    if request.method == 'POST':
        user = request.user
        if user.pro_status != 'pro':
            user.pro_status = 'pro'
            user.save()
            messages.success(request, 'Поздравляем! Теперь у вас PRO-статус')
            return redirect('users:profile')

    # Если GET-запрос или что-то пошло не так
    return redirect('users:profile')


def leaderboard(request):
    rankings = UserRanking.objects.select_related('user').order_by('-total_score')

    return render(request, 'users/leaderboard.html', {
        'rankings': rankings
    })
