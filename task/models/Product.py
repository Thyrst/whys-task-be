from django.db import models


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    cena = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    is_published = models.BooleanField(default=None, null=True, blank=True)
    mena = models.CharField(max_length=255, null=True, blank=True)
    nazev = models.CharField(max_length=255, null=True, blank=True)
    published_on = models.CharField(max_length=255, null=True, blank=True)
