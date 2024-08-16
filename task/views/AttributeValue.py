from rest_framework import viewsets
from task.models import AttributeValue
from task.serializers import AttributeValueSerializer


class AttributeValueViewSet(viewsets.ModelViewSet):
    queryset = AttributeValue.objects.all()
    serializer_class = AttributeValueSerializer
