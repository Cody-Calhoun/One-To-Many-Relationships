from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50)
    wins = models.IntegerField()
    location = models.CharField(max_length=50)
    mascot = models.CharField(max_length=45)
    # current_players
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Player(models.Model):
    name = models.CharField(max_length=50)
    jersey_number = models.IntegerField()
    position = models.CharField(max_length=50)
    batting_avg = models.IntegerField()
    current_team = models.ForeignKey(Team, related_name = "current_players", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)