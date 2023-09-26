from django.db import models

# Create your models here.


class Player(models.Model):
    NTRP = [
        ("<2.0", "<2.0"),
        ("2.5", "2.5"),
        ("3.0", "3.0"),
        ("3.5", "3.5"),
        ("4.0", "4.0"),
        ("4.5", "4.5"),
        ("5.0", "5.0"),
        (">5.0", ">5.0"),
    ]
    first_name = models.CharField(max_length=150)
    second_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150)
    birth_date = models.DateField(blank=True, null=True)
    nick_name = models.CharField(max_length=150, blank=True)
    ntrp = models.CharField(max_length=10, choices=NTRP)
    email = models.EmailField()
    phone = models.CharField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
