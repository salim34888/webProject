from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.views.decorators.http import require_GET
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('ai/', include('aichat.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tests/', include('tests.urls')),
    path('knowledge/', include('knowledge.urls')),
    path('analytics/', include('analytics.urls')),
    path('support/', include('support.urls')),
    path('accounts/logout/', require_GET(LogoutView.as_view()), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)