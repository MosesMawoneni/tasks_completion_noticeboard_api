from django.db import models
from django.conf import settings


# The TimeStamp class is a model that represents a time interval with a start and end date, where the
# start date is automatically set when the object is created and the end date is automatically updated
# whenever the object is modified.
class TimeStamp(models.Model):
    date_started = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


        
class Task(TimeStamp):
    """
    The above code defines a Task model with various fields such as worker, task_name,
    task_description, complete, and other_explanation.
    :return: The `__str__` method is returning the `task_name` attribute of the Task object.
    """
    worker = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='tasks')
    task_name = models.CharField(max_length=255)
    task_description = models.TextField()
    complete  = models.BooleanField(default=False)
    other_explanation = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "tasks"

    def __str__(self):
        return self.task_name



