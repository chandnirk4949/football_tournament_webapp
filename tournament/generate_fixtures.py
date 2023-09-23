import itertools
import random
from datetime import datetime, time, timedelta

from .models import Fixtures, Teams


# function to generate fixtures automatically with the predefined data of 5 venues and in the predefined time span
def generate_fixtures():
    # Define the teams
    teams = Teams.objects.all()

    # Define the start and end dates for the tournament (hard-coded values)
    start_date = datetime(2023, 9, 15)
    end_date = datetime(2023, 10, 30)

    # Define match times
    match_time_1 = time(10, 0)  # Example: 10:00 AM
    match_time_2 = time(15, 0)  # Example: 3:00 PM

    # Define 5 venues
    venues = [
        "Lulu stadium, Palarivattom",
        "Adam stadium, Edappally",
        "Forum stadium, Vennala",
        "Oberon stadium, Kaloor",
        "Grand Central stadium, Fort Kochi",
    ]

    # Initialize variables
    fixtures = []
    current_date = start_date
    venues_used = set()  # To track which venues have been used

    # Generate all possible combinations of team pairs
    team_pairs = list(itertools.combinations(teams, 2))

    # Shuffle the team pairs to randomize the fixture order
    random.shuffle(team_pairs)

    # Create a dictionary to track each team's last match date and time
    last_match_datetime = {team: None for team in teams}

    # Generate the fixtures while considering rest days, times, and venues
    while current_date <= end_date and team_pairs:
        matches_on_current_date = []
        available_teams = set(teams)

        for team1, team2 in team_pairs:
            if team1 in available_teams and team2 in available_teams:
                # Check if both teams have had a rest day
                if (
                    last_match_datetime[team1] is None
                    or (current_date - last_match_datetime[team1]).days > 1  # type: ignore
                ) and (
                    last_match_datetime[team2] is None
                    or (current_date - last_match_datetime[team2]).days > 1  # type: ignore
                ):
                    # Determine the match time based on the number of matches scheduled on the current date
                    match_time = (
                        match_time_1
                        if len(matches_on_current_date) % 2 == 0
                        else match_time_2
                    )
                    match_datetime = datetime.combine(current_date, match_time)

                    # Randomly choose a venue that hasn't been used yet
                    unused_venues = set(venues) - venues_used
                    if unused_venues:
                        selected_venue = random.choice(list(unused_venues))
                        venues_used.add(selected_venue)
                    else:
                        # If all venues have been used, reset the set of used venues
                        venues_used.clear()
                        selected_venue = random.choice(venues)

                    matches_on_current_date.append(
                        (team1, team2, match_datetime, selected_venue)
                    )
                    available_teams.remove(team1)
                    available_teams.remove(team2)
                    team_pairs.remove((team1, team2))

                    if len(matches_on_current_date) >= 2:
                        break

        if matches_on_current_date:
            for match in matches_on_current_date:
                fixtures.append(
                    {
                        "team1": match[0],
                        "team2": match[1],
                        "venue": match[3],
                        "date_time": match[2],
                    }
                )
                last_match_datetime[match[0]] = match[2]
                last_match_datetime[match[1]] = match[2]

        current_date += timedelta(days=1)  # Move to the next day

    for fixture in fixtures:
        team1 = fixture["team1"]
        team2 = fixture["team2"]
        venue = fixture["venue"]
        date_time = fixture["date_time"]

        # Create the Fixture
        Fixtures.objects.create(
            team1=team1, team2=team2, venue=venue, date_time=date_time
        )
