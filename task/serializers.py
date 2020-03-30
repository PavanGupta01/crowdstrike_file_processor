from rest_framework import serializers

from django.contrib.auth.models import User, Group
from task.models import Task


class TaskSerializer(serializers.Serializer):

    task_id = serializers.CharField(max_length=128)
    file_id = serializers.UUIDField()
    status = serializers.ChoiceField(choices=Task.TASK_STATUS)
    result = serializers.JSONField()

    class Meta:
        model = Task
