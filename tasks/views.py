from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from tasks.models import Task

# Create your views here.

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'

