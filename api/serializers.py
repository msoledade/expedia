from api.models import Process
from rest_framework import serializers


class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = ('name', 'type', 'number', 'created_at')
