from django.db import models
from task.models import AttributeName, AttributeValue


class Attribute(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev_atributu_id = models.ForeignKey(
        AttributeName, on_delete=models.SET_NULL, null=True, blank=True
    )
    hodnota_atributu_id = models.ForeignKey(
        AttributeValue, on_delete=models.SET_NULL, null=True, blank=True
    )
