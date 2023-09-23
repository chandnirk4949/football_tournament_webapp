from django.shortcuts import get_object_or_404, render, redirect
from django.forms import formset_factory
from django.contrib.auth import authenticate, login, logout
from .generate_fixtures import generate_fixtures
from .models import Fixtures, Scores, Teams, Team_members
from .forms import ScoreEditForm, TeamMemberForm
from django.contrib import messages
from django.core.exceptions import ValidationError
def home(request):
        # Get the count of registered teams
    registered_teams_count = Teams.objects.count()
    return render(request, "tournament/index.html", {'registered_teams_count': registered_teams_count})

def register_team(request):
    if request.method == "POST":
        form = TeamMemberForm(request.POST)

        if form.is_valid():
            team_name = form.cleaned_data["team_name"]
            member_names = request.POST.getlist("member_name")
            roles = request.POST.getlist("member_role")

            team = Teams.objects.create(name=team_name)

            for member, role in zip(member_names, roles):
                name = member
                role = role.lower()
                Team_members.objects.create(name=name, role=role, team=team)

            if Teams.objects.count() >= 10:
                generate_fixtures()
                # Display a success message
            messages.success(request, "Team successfully registered!")
            return redirect("/")
        else:
            # Render the form again with the validation errors displayed
            for errors in form.errors.values():
                for error in errors:
                    messages.error(request, f"{error}")
            return render(request, "tournament/register_team.html", {'form': form})

    else:
        form = TeamMemberForm()

    return render(request, "tournament/register_team.html", {'form': form})

def admmin_login(request):
    if request.method == "POST":
        name = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)  # type: ignore
            messages.success(request, "logged in successfully!")
            return redirect("/")
        else:
            return redirect("login")
    else:
        return render(request, "tournament/admin_login.html")

def admin_logout(request):
    logout(request)
    messages.success(request, "logged out successfully!")
    return redirect('/')

from django.shortcuts import render
from .models import Fixtures, Scores, Teams

def fixture_data(request):
    fixtures = Fixtures.objects.all()

    # Get the total number of teams registered
    registered_teams_count = Teams.objects.count()

    # Check if there are any fixtures scheduled
    if not fixtures.exists():
        # Display the "only __ teams got registered. fixtures will be scheduled when registration completes." message
        return render(request, "tournament/fixtures.html", {'registered_teams_count': registered_teams_count})

    # Create a dictionary to store fixture data with scores
    fixture_data = {}

    # Iterate through fixtures and get scores
    for fixture in fixtures:
        team1_score = Scores.objects.filter(fixture=fixture, team=fixture.team1).first()
        team2_score = Scores.objects.filter(fixture=fixture, team=fixture.team2).first()
        fixture_data[fixture.id] = { # type: ignore
            'team1_name': fixture.team1.name,
            'team2_name': fixture.team2.name,
            'venue': fixture.venue,
            'date_time': fixture.date_time,
            'team1_score': team1_score.score if team1_score else None,
            'team2_score': team2_score.score if team2_score else None,
        }

    # Otherwise, display the fixtures data
    return render(request, "tournament/fixtures.html", {'fixtures': fixture_data})

def team_data(request):
    teams = Teams.objects.all()
    members = Team_members.objects.all()
    return render(request, "tournament/teams.html", {'teams': teams, 'members':members})

def edit_score(request, fixture_id):
    fixture = get_object_or_404(Fixtures, pk=fixture_id)

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = ScoreEditForm(request.POST)
        if form.is_valid():
            # Get a reference to the Scores model instances for the team1 and team2 teams
            team1_score, _ = Scores.objects.get_or_create(fixture=fixture, team=fixture.team1)
            team2_score, _ = Scores.objects.get_or_create(fixture=fixture, team=fixture.team2)

            # Update the scores
            team1_score.score = form.cleaned_data['team1_score']
            team2_score.score = form.cleaned_data['team2_score']

            # Save the changes
            team1_score.save()
            team2_score.save()

            return redirect('fixtures')  # Redirect to the fixture list page after editing
        else:
            # Render the form again with the validation errors displayed
            for errors in form.errors.values():
                for error in errors:
                    messages.error(request, f"{error}")
            return redirect('edit_score',fixture_id=fixture_id)
    else:
        initial_data = {
            'team1_score': Scores.objects.get_or_create(fixture=fixture, team=fixture.team1)[0].score,
            'team2_score': Scores.objects.get_or_create(fixture=fixture, team=fixture.team2)[0].score,
        }

        form = ScoreEditForm(initial=initial_data)

    context = {
        'fixture': fixture,
        'form': form,
    }
    return render(request, 'tournament/edit_score.html', context)
