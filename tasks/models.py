from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    STATUS_CHOISES = [
        ('todo', 'To do'),
        ('in_progress', 'In progress'),
        ('done', 'Done'),
    ]
    PRIORITY_CHOISES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    title = models.CharField(max_length=63)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=63, choices=STATUS_CHOISES, default='todo')
    priority = models.CharField(max_length=63, choices=PRIORITY_CHOISES, default='medium')
    due_data = models.DateTimeField(blank=True, null=True)

    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
