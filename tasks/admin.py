from django.contrib import admin

from . import models

@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['worker','task_name','task_description']
