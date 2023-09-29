from django.db import models

from games.models.game import Game


class Exercise(models.Model):
    TYPES = [
        ("Forehand Cross", "Forehand Cross"),
        ("Forehand Line", "Forehand Line"),
        ("Forehand Attack", "Forehand Attack"),
        ("Forehand Volley", "Forehand Volley"),
        ("Forehand Drop shot", "Forehand Drop shot"),
        ("Backhand Cross", "Backhand Cross"),
        ("Backhand Line", "Backhand Line"),
        ("Backhand Attack", "Backhand Attack"),
        ("Backhand Volley", "Backhand Volley"),
        ("Backhand Drop shot", "Backhand Drop shot"),
        ("Smatch", "Smatch"),
        ("Service", "Service"),
        ("Game", "Game"),
    ]
    type = models.CharField(max_length=100, choices=TYPES)
    duration = models.DurationField()
    additional_info = models.CharField(max_length=2000, choices=TYPES)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
