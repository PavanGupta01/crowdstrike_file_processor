from django.shortcuts import render
from django.core import serializers
from django.core.cache import cache
# from django.contrib.auth.models import User, Group

# Create your views here.
from rest_framework import status as http_status_code
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import filters

from task.models import Task
from task.serializers import TaskSerializer
from task.tasks import sum, analyze_file

class TaskView(APIView):
    # search_fields = ['file_id']
    # filter_backends = (filters.SearchFilter,)

    def get(self, request, task_id=None):

        if task_id:
             tasks = Task.objects.filter(task_id = task_id)
             serializer = TaskSerializer(tasks, many=True)
        else:
            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks, many=True)

        return Response(serializer.data, status=http_status_code.HTTP_200_OK)

    def post(self, request):

        task_serializer = TaskSerializer(data=request.data)

        if not task_serializer.is_valid():
            return Response(task_serializer.errors,
                            status=http_status_code.HTTP_400_BAD_REQUEST)
        
        validated_data = task_serializer.validated_data
        task = Task.objects.create(
                            task_id = validated_data.get('task_id'),
                            file_id = validated_data.get('file_id'),
                            status = validated_data.get('status'), 
                            result = validated_data.get('result')
                )

        # # Cache
        # cache_key = 'task_id'
        # cache.set(cache_key, "First Task for analysis")

        # Async call for analysing file.
        analyze_file.delay(validated_data.get('task_id'))

        return Response(task_serializer.data, status=http_status_code.HTTP_201_CREATED)


