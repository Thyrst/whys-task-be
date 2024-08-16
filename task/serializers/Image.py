from rest_framework import serializers
from task.models import Image
from task.serializers.mixins import CreateOrUpdateMixin


class ImageSerializer(CreateOrUpdateMixin, serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Image
        fields = ["id", "obrazek", "nazev"]
