from django.db import models

from clubs.models import Court
from players.models import Player

# Create your models here.


class Game(models.Model):
    TYPES = [
        ("Friendly", "Friendly"),
        ("Training", "Training"),
        ("League", "League"),
    ]
    type = models.CharField(max_length=50, choices=TYPES)
    duration = models.DurationField()
    host = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="host")
    opponent = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="opponent"
    )
    court = models.ForeignKey(Court, on_delete=models.SET_NULL, null=True, blank=True)
    result = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
