from rest_framework import viewsets
from task.models import Attribute
from task.serializers import AttributeSerializer


class AttributeViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
