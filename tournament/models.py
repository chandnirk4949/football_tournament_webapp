from django.db import models

# Create your models here.

from django.db import models

class Teams(models.Model):
    name = models.CharField(max_length=200)

class Team_members(models.Model):
    ROLE_CHOICES = (
        ('player', 'Player'),
        ('coach', 'Coach'),
        ('manager', 'Manager'),
    )
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)

class Fixtures(models.Model):
    team1 = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='team1')
    team2 = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='team2')
    venue = models.CharField(max_length=200)
    date_time = models.DateTimeField()

class Scores(models.Model):
    fixture = models.ForeignKey(Fixtures, on_delete=models.CASCADE, related_name='fixture')
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name='team_score')
    score = models.IntegerField(null=True, blank=True)


    