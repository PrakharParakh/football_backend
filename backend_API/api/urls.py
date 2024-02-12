from django.urls import path
from . import views

urlpatterns = [
    path('fixtures',views.getFixtures),
    path('league',views.getLeague),
    path('standings',views.getStandings),
    path('teams',views.getTeams),
    path('statistics',views.getFixturesStatistics),
    path('events',views.getFixturesEvents),
    path('head-to-head',views.getHeadToHead),
    path('lineup',views.getLineup),
    path('predictions',views.getPredictions),
    path('daily-quiz', views.dailyQuiz)
]