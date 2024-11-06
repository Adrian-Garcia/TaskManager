from django.urls import path
from .views import (
    IndexView,
    detail,
    update,
    new,
    create,
    delete,
    get_tasks,
    create_task,
    update_task,
    delete_task,
)

app_name = "tasks"

urlpatterns = [
    # ex: /tasks/
    path("tasks/", IndexView.as_view(), name="index"),
    # ex: /tasks/new/
    path("tasks/new/", new, name="new"),
    # ex: /tasks/create/
    path("tasks/create/", create, name="create"),
    # ex: /tasks/1/
    path("tasks/<int:task_id>/", detail, name="detail"),
    # ex: /tasks/update/1/
    path("tasks/update/<int:task_id>/", update, name="update"),
    # ex: /tasks/delete/1/
    path("tasks/delete/<int:task_id>/", delete, name="delete"),
    # ex: GET /api/tasks/
    path("api/tasks/", get_tasks, name="get_tasks"),
    # ex: POST /api/tasks/post/
    path("api/tasks/post/", create_task, name="create_task"),
    # ex: PUT /api/tasks/1/
    path("api/tasks/<int:task_id>/", update_task, name="update_task"),
    # ex: DELETE /api/tasks/delete/1/
    path("api/tasks/delete/<int:task_id>/", delete_task, name="delete_task"),
]
