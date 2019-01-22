from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('index', permanent=False)),
    path('bets/', include('bets.urls')),
    path('admin/', admin.site.urls),
]
