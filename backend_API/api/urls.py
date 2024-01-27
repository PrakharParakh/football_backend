from django.urls import path
from . import views

urlpatterns = [
    path('fixtures',views.getFixtures),
    path('league',views.getLeague),
    path('standings',views.getStandings),
    path('teams',views.getTeams),
    path('statistics',views.getFixturesStatistics),
    path('events',views.getFixturesEvents)
]