from django.db import models
from task.models import Product, Image


class ProductImage(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True
    )
    obrazek_id = models.ForeignKey(
        Image, on_delete=models.SET_NULL, null=True, blank=True
    )
    nazev = models.CharField(max_length=255, null=True, blank=True)
