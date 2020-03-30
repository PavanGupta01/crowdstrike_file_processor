from django.core.cache import cache

from rest_framework import status as http_status_code
from rest_framework.response import Response
from rest_framework.views import APIView

from task.models import Task
from task.serializers import TaskSerializer
from task.tasks import analyze_file

class TaskView(APIView):

    def get(self, request, task_id=None):
        
        file_id = request.GET.get('uuid')
        
        if file_id:
            tasks = Task.objects.filter(file_id = file_id)

        elif task_id:
            tasks = Task.objects.filter(task_id = task_id)
    
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


