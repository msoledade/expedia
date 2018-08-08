from api.models import Process
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    processes = serializers.PrimaryKeyRelatedField(many=True, queryset=Process.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'processes')


class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = ('owner', 'name', 'type', 'number', 'created_at')
        owner = serializers.ReadOnlyField(source='owner.username')
