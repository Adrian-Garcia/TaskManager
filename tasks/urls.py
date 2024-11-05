from django.urls import path
from .views import IndexView, detail, update, new, create, delete

app_name = "tasks"

urlpatterns = [
    # ex: /tasks/
    path("", IndexView.as_view(), name="index"),
    # ex: /tasks/new/
    path("new/", new, name="new"),
    # ex: /tasks/create/
    path("create/", create, name="create"),
    # ex: /tasks/1/
    path("<int:task_id>/", detail, name="detail"),
    # ex: PUT /tasks/1/
    path("update/<int:task_id>/", update, name="update"),
    # ex: DELETE /tasks/1/
    path("delete/<int:task_id>/", delete, name="delete"),
]
