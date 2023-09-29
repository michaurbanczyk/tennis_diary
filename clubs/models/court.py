from django.db import models

from .club import Club


class Court(models.Model):
    TYPES = [
        ("Clay", "Clay"),
        ("Synthetic Clay", "Synthetic Clay"),
        ("Grass", "Grass"),
        ("Synthetic Grass", "Synthetic Grass"),
        ("Hard", "Hard"),
        ("Other", "Other"),
    ]
    type = models.CharField(max_length=50, choices=TYPES)
    is_doubles = models.BooleanField()
    is_lighting = models.BooleanField()
    is_indoor = models.BooleanField()
    is_winter_indoor = models.BooleanField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
