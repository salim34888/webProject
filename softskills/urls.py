from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tests/', include('tests.urls')),
    path('knowledge/', include('knowledge.urls')),
    path('analytics/', include('analytics.urls')),
    path('support/', include('support.urls')),
]