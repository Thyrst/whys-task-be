from rest_framework import serializers
from task.models import Attribute
from task.serializers.mixins import CreateOrUpdateMixin


class AttributeSerializer(CreateOrUpdateMixin, serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Attribute
        fields = ["id", "nazev_atributu_id", "hodnota_atributu_id"]
