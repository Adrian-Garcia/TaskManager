from django.shortcuts import render
from .models import Task
from django.views import generic
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .helpers import get_update_errors, get_create_errors


class IndexView(generic.ListView):
    template_name = "tasks/index.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.all


def detail(request: WSGIRequest, task_id: int) -> HttpResponse:
    task = get_object_or_404(Task, pk=task_id)
    return render(request, "tasks/detail.html", {"task": task})


def new(request: WSGIRequest) -> HttpResponse:
    task = Task()
    return render(request, "tasks/new.html", {"task": task, "errors": []})


def create(request: WSGIRequest) -> HttpResponseRedirect:
    task = Task(
        title=request.POST["title"],
        description=request.POST["description"],
        email=request.POST["email"],
    )

    errors = get_create_errors(task)

    if not errors:
        task.save()
        return HttpResponseRedirect(reverse("tasks:detail", args=(task.id,)))

    return render(
        request,
        "tasks/new.html",
        {"task": task, "errors": errors},
    )


def update(request: WSGIRequest, task_id: int):
    task = get_object_or_404(Task, pk=task_id)
    errors = get_update_errors(request)

    if not errors:
        task.title = request.POST["title"]
        task.description = request.POST["description"]

        task.save()
        return HttpResponseRedirect(reverse("tasks:index"))

    return render(
        request,
        "tasks/detail.html",
        {"task": task, "errors": errors},
    )


def delete(request, task_id: int) -> HttpResponseRedirect:
    task = get_object_or_404(Task, pk=task_id)
    task.delete()

    return HttpResponseRedirect(reverse("tasks:index"))
