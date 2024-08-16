from rest_framework import serializers
from task.models import ProductImage
from task.serializers.mixins import CreateOrUpdateMixin


class ProductImageSerializer(CreateOrUpdateMixin, serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = ProductImage
        fields = ["id", "product", "obrazek_id", "nazev"]
