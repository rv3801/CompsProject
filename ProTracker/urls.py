from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:team_code>/', views.team, name = 'team'),
    path('player/<str:player_ign>/', views.player, name = 'player'),
]