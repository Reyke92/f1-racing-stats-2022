from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.viewIndex, name='index'),
    path('drivers/', views.viewDriverRanking, name='drivers'),
    path('races/', views.viewRaceRanking, name='races'),
    path('teams/', views.viewTeamRanking, name='teams'),
]
