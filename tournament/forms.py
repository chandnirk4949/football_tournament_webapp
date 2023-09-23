from django import forms
from django.core.exceptions import ValidationError

# create your forms here


# form for team registration
class TeamMemberForm(forms.Form):
    team_name = forms.CharField(max_length=100, label="Team Name", required=False)
    member_name = forms.CharField(max_length=100, label="Member Name", required=False)
    member_role = forms.ChoiceField(
        choices=[("player", "Player"), ("manager", "Manager"), ("coach", "Coach")],
        required=False,
    )

    def clean(self):
        cleaned_data = super().clean()
        if "member_role" and "member_name" in self.data:
            num_players = 0
            num_coaches = 0
            num_managers = 0
            for member_role in self.data.getlist("member_role"):  # type: ignore
                if member_role == "player":
                    num_players += 1
                elif member_role == "coach":
                    num_coaches += 1
                elif member_role == "manager":
                    num_managers += 1

            # Validate the minimum number of players, coach, and manager
            if num_players < 11:
                raise ValidationError("Each team must have at least 11 players.")
            elif num_coaches < 1:
                raise ValidationError("Each team must have at least 1 coach.")
            elif num_managers < 1:
                raise ValidationError("Each team must have at least 1 manager.")
        else:
            raise ValidationError("No members were added to the team.")
        return cleaned_data


# form for the score edit
class ScoreEditForm(forms.Form):
    team1_score = forms.IntegerField(label="Team 1 Score", required=True)
    team2_score = forms.IntegerField(label="Team 2 Score", required=True)

    def clean(self):
        cleaned_data = super().clean()
        # cheching for -ve values of scores
        if not (
            cleaned_data.get("team1_score", -1) >= 0
            and cleaned_data.get("team2_score", -1) >= 0
        ):
            raise ValidationError("score value can not be -ve")
        return cleaned_data
