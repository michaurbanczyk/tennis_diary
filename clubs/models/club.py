from django.db import models

from .address import Address


class Club(models.Model):
    name = models.CharField(max_length=250)
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    additional_info = models.TextField(max_length=2000)
