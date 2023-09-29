from django.db import models


class Address(models.Model):
    COUNTRIES = [("PL", "POLAND")]
    street_name_1 = models.CharField(max_length=150)
    street_name_2 = models.CharField(max_length=150, blank=True, null=True)
    home_number = models.CharField(max_length=20)  # CharField to handle case like 81A
    flat_number = models.CharField(max_length=20, blank=True, null=True)
    zip_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=10, choices=COUNTRIES)
