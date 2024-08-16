from rest_framework import viewsets
from rest_framework.response import Response
from task.serializers import ImportDataSerializer
from task.serializers.Attribute import AttributeSerializer
from task.serializers.AttributeName import AttributeNameSerializer
from task.serializers.AttributeValue import AttributeValueSerializer
from task.serializers.Catalog import CatalogSerializer
from task.serializers.Image import ImageSerializer
from task.serializers.Product import ProductSerializer
from task.serializers.ProductAttributes import ProductAttributesSerializer
from task.serializers.ProductImage import ProductImageSerializer


def validate_and_upsert(serializer, data):
    serializer_instance = serializer(data=data)
    if serializer_instance.is_valid():
        serializer_instance.create_or_update(serializer_instance.validated_data)
        return {"status": "success"}
    else:
        return {"status": "error", "errors": serializer_instance.errors}


def process_data(items, serializer_class, results, key):
    for index, item in enumerate(items):
        if key in item:
            results[index] = results[index] or {}
            results[index][key] = validate_and_upsert(serializer_class, item[key])


class ImportDataViewSet(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = ImportDataSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        results = [None] * len(data)

        process_data(data, AttributeNameSerializer, results, "AttributeName")
        process_data(data, AttributeValueSerializer, results, "AttributeValue")
        process_data(data, AttributeSerializer, results, "Attribute")
        process_data(data, ImageSerializer, results, "Image")
        process_data(data, ProductSerializer, results, "Product")
        process_data(data, ProductAttributesSerializer, results, "ProductAttributes")
        process_data(data, ProductImageSerializer, results, "ProductImage")
        process_data(data, CatalogSerializer, results, "Catalog")

        return Response(results, status=201)
