from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm
from .models import User  # Убедитесь, что модель User импортирована


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
        user = self.request.user

        # Основная информация
        context.update({
            'goals': user.usergoal_set.all(),
            'test_results': user.testresult_set.all(),
            'pro_status': user.pro_status,
        })

        # PRO-статистика
        if user.pro_status == 'pro':
            context['pro_features'] = {
                'tests_completed': user.testresult_set.count(),
                'articles_read': user.userfavorite_set.count(),
            }

        return context


@login_required
def upgrade_to_pro(request):
    if request.method == 'POST':
        user = request.user
        if user.pro_status != 'pro':
            # Здесь должна быть реальная логика оплаты
            user.pro_status = 'pro'
            user.save()
            messages.success(request, 'PRO-статус успешно активирован!')
        else:
            messages.info(request, 'У вас уже активирован PRO-статус')
        return redirect('profile')

    messages.error(request, 'Неверный запрос')
    return redirect('profile')
