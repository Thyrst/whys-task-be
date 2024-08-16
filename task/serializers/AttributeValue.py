from rest_framework import serializers
from task.models import AttributeValue
from task.serializers.mixins import CreateOrUpdateMixin


class AttributeValueSerializer(CreateOrUpdateMixin, serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = AttributeValue
        fields = ["id", "hodnota"]
