from django.urls import path
from tasks.views import TaskDetailView, TaskListView

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('<pk:int>', TaskDetailView.as_view(), name='task-detail'),
]

app_name = 'tasks'