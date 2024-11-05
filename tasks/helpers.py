from django.core.handlers.wsgi import WSGIRequest
from .models import Task


def get_update_errors(request: WSGIRequest):
    errors = []

    if request.POST["title"] == "":
        errors.append("Title can not be empty")

    if request.POST["description"] == "":
        errors.append("Description can not be empty")

    return errors


def get_create_errors(task: Task):
    errors = []

    if task.title == "":
        errors.append("Title can not be empty")

    if task.description == "":
        errors.append("Description can not be empty")

    if task.email == "":
        errors.append("Email can not be empty")

    return errors
