from rest_framework import viewsets
from task.models import AttributeName
from task.serializers import AttributeNameSerializer


class AttributeNameViewSet(viewsets.ModelViewSet):
    queryset = AttributeName.objects.all()
    serializer_class = AttributeNameSerializer
