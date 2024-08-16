from rest_framework import viewsets
from task.models import ProductAttributes
from task.serializers import ProductAttributesSerializer


class ProductAttributesViewSet(viewsets.ModelViewSet):
    queryset = ProductAttributes.objects.all()
    serializer_class = ProductAttributesSerializer
