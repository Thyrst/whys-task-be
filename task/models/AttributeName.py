from django.db import models


class AttributeName(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length=255, null=True, blank=True)
    kod = models.CharField(max_length=255, null=True, blank=True)
    zobrazit = models.BooleanField(default=None, null=True, blank=True)
