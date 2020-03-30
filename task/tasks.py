from __future__ import absolute_import
import uuid

from file_processor.celery import app
from task.models import Task

@app.task
def analyze_file(task_id):
    task = Task.objects.get(task_id = task_id)
    task.status = Task.COMPLETED
    # Adding 3 random uuids as ref instead of extracting from file.
    task.result = {"reference_file_ids":[str(uuid.uuid4()) for i in range(3)]}
    task.save()


