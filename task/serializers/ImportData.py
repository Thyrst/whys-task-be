from rest_framework import serializers


class ImportDataSerializer(serializers.ListSerializer):
    child = serializers.DictField()
