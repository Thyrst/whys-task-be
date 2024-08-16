from rest_framework import serializers
from task.models import Product
from task.serializers.mixins import CreateOrUpdateMixin


class ProductSerializer(CreateOrUpdateMixin, serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Product
        fields = [
            "id",
            "cena",
            "description",
            "is_published",
            "mena",
            "nazev",
            "published_on",
        ]
