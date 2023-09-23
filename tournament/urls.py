# tournament/urls.py

from django.urls import path

from .views import (
    admin_logout,
    admmin_login,
    edit_score,
    fixture_data,
    home,
    register_team,
    team_data,
)

# provide urls for all the functionalities here
urlpatterns = [
    path("", home, name="home"),  # home page
    path("login/", admmin_login, name="login"),  # admin login page
    path("logout/", admin_logout, name="logout"),  # admin logout function
    path("register/", register_team, name="register_team"),  # register team page
    path("fixtures/", fixture_data, name="fixtures"),  # fixtures data page
    path(
        "fixtures/edit_score/<int:fixture_id>/", edit_score, name="edit_score"
    ),  # edit score page
    path("teams/", team_data, name="teams"),  # team data page
]
