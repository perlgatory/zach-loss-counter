from django.urls import path

from . import views

urlpatterns = [
    # ex: /bets/
    path('', views.index, name='index'),
    # ex: /bets/1/
    path('<int:bet_id>/', views.detail, name='detail'),
]
