from django.db import models


class Image(models.Model):
    id = models.IntegerField(primary_key=True)
    obrazek = models.CharField(max_length=255)
    nazev = models.CharField(max_length=255, null=True, blank=True)
