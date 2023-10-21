from django.urls import path, include
from rest_framework.routers import DefaultRouter

from teams import views

team_router = DefaultRouter()
team_router.register(prefix='teams', viewset=views.TeamViewSet, basename='teams')
team_router.register(prefix='persons', viewset=views.PersonViewSet, basename='persons')

urlpatterns = [
    path('', include(team_router.urls))
]
