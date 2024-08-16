from rest_framework import serializers
from task.models import ProductAttributes
from task.serializers.mixins import CreateOrUpdateMixin


class ProductAttributesSerializer(CreateOrUpdateMixin, serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = ProductAttributes
        fields = ["id", "attribute", "product"]
