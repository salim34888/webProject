from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.views.decorators.http import require_GET

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tests/', include('tests.urls')),
    path('knowledge/', include('knowledge.urls')),
    path('analytics/', include('analytics.urls')),
    path('support/', include('support.urls')),
    path('accounts/logout/', require_GET(LogoutView.as_view()), name='logout'),
]