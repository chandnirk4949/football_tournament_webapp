# tournament/urls.py

from django.urls import path
from .views import admin_logout, admmin_login, edit_score, fixture_data, home, register_team,team_data

from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('login/', admmin_login, name='login'),
    path('logout/', admin_logout, name='logout'),
    path('register/', register_team, name='register_team'),
    path('fixtures/', fixture_data, name='fixtures'),
    path('fixtures/edit_score/<int:fixture_id>/', edit_score, name='edit_score'),
    path('teams/', team_data, name='teams'),
    # Add other URLs for admin login, fixture details, etc.
]
