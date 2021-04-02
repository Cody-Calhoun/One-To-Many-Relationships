from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('newTeam', views.new_team),
    path('newPlayer', views.new_player)
]