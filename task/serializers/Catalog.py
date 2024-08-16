from rest_framework import serializers
from task.models import Catalog
from task.serializers.Attribute import AttributeSerializer
from task.serializers.Product import ProductSerializer
from task.serializers.mixins import CreateOrUpdateMixin


class ReadThumbCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = [
            "id",
            "nazev",
            "obrazek_id",
        ]


class ReadCatalogSerializer(serializers.ModelSerializer):
    products_ids = ProductSerializer(many=True)
    attributes_ids = AttributeSerializer(many=True)

    class Meta:
        model = Catalog
        fields = [
            "id",
            "nazev",
            "obrazek_id",
            "products_ids",
            "attributes_ids",
        ]


class CatalogSerializer(CreateOrUpdateMixin, serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Catalog
        fields = [
            "id",
            "nazev",
            "obrazek_id",
            "products_ids",
            "attributes_ids",
        ]
