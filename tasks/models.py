from django.db import models
from django.conf import settings


class TimeStamp(models.Model):
    date_started = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
class Task(TimeStamp):
    worker = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='tasks')
    task_name = models.CharField(max_length=255)
    task_description = models.TextField()
    complete  = models.BooleanField(default=False)
    other_explanation = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "tasks"

    def __str__(self):
        return self.task_name



