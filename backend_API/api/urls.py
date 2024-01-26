from django.urls import path
from . import views

urlpatterns = [
    path('',views.getFixtures),
    path('',views.getLeague),
    path('',views.getStandings),
]