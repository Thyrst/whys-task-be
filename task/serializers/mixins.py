from rest_framework import serializers


class CreateOrUpdateMixin:
    def create_or_update(self, validated_data):
        try:
            instance = self.Meta.model.objects.get(id=validated_data["id"])
        except self.Meta.model.DoesNotExist:
            return self.create(validated_data)
        else:
            self.update(instance, validated_data)
