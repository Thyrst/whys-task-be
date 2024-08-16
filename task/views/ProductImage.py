from rest_framework import viewsets
from task.models import ProductImage
from task.serializers import ProductImageSerializer


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
