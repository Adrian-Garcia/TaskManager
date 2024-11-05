from django.urls import path
from .views import IndexView, detail

app_name = "tasks"

urlpatterns = [
    # ex: /tasks/
    path("", IndexView.as_view(), name="index"),

    # ex: /tasks/1/
    path("<int:pk>/", detail, name="detail")
]
