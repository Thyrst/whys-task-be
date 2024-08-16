from rest_framework import serializers
from task.models import AttributeName
from task.serializers.mixins import CreateOrUpdateMixin


class AttributeNameSerializer(CreateOrUpdateMixin, serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = AttributeName
        fields = ["id", "nazev"]
