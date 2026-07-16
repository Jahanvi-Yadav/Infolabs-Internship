from django.db import models

# Create your models here.
from django.db import models


class Team(models.Model):
    team_name = models.CharField(max_length=100)
    coach_name = models.CharField(max_length=100)
    captain_name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_name


class Player(models.Model):
    team_id = models.ForeignKey(
        Team,
        on_delete=models.CASCADE
    )
    player_name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    age = models.IntegerField()
    country = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.player_name