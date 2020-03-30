from django.db import models

# Create your models here.
class Task(models.Model):

    STARTED = 1
    IN_PROGRESS = 2
    COMPLETED = 3

    TASK_STATUS = (
        (1, STARTED),
        (2, IN_PROGRESS),
        (3, COMPLETED)
    )

    task_id = models.CharField(max_length = 128, db_index=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    file_id = models.UUIDField()
    status = models.SmallIntegerField(choices=TASK_STATUS, default=COMPLETED)
    result = models.TextField()