from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('bets/', include('bets.urls')),
    path('admin/', admin.site.urls),
]