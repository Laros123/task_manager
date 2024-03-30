from django.urls import path
from tasks.views import TaskDetailView, TaskListView, TaskCreateView

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task-create/', TaskCreateView.as_view(), name='task-create'),
]

app_name = 'tasks'