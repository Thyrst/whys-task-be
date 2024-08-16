from rest_framework import viewsets
from task.models import Catalog
from task.serializers import ReadCatalogSerializer, ReadThumbCatalogSerializer


class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = ReadThumbCatalogSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ReadCatalogSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        if self.action == "retrieve":
            return Catalog.objects.prefetch_related(
                "products_ids", "attributes_ids"
            ).all()
        return super().get_queryset()
