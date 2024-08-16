from django.db import models
from task.models import Product, Attribute, Image


class Catalog(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length=255, null=True, blank=True)
    obrazek_id = models.ForeignKey(
        Image, on_delete=models.SET_NULL, null=True, blank=True
    )
    products_ids = models.ManyToManyField(Product, blank=True)
    attributes_ids = models.ManyToManyField(Attribute, blank=True)
