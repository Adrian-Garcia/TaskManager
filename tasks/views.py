from django.shortcuts import render
from .models import Task
from django.views import generic
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .helpers import get_update_errors, get_create_errors
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

# ex: /tasks/
class IndexView(generic.ListView):
    template_name = "tasks/index.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.all


# ex: /tasks/1/
def detail(request: WSGIRequest, task_id: int) -> HttpResponse:
    task = get_object_or_404(Task, pk=task_id)
    return render(request, "tasks/detail.html", {"task": task})


# ex: /tasks/new/
def new(request: WSGIRequest) -> HttpResponse:
    task = Task()
    return render(request, "tasks/new.html", {"task": task, "errors": []})


# ex: /tasks/create/
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


# ex: /tasks/update/1/
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


# ex: /tasks/delete/1/
def delete(request, task_id: int) -> HttpResponseRedirect:
    task = get_object_or_404(Task, pk=task_id)
    task.delete()

    return HttpResponseRedirect(reverse("tasks:index"))


# ex: GET /api/tasks
@api_view(["GET"])
def get_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


# ex: POST /api/tasks
@api_view(["POST"])
def create_task(request):
    print("======== 0 ========")

    if not request.data.get("title") or not request.data.get("description"):
        return Response(
            {"error": "Both title and description are required."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    print("======== 1 ========")

    serializer = TaskSerializer(data=request.data)
    print("======== 2 ========")
    if serializer.is_valid():
        print("======== 3 ========")
        serializer.save()
        print("======== 4 ========")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print("======== 5 ========")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ex: PUT /api/tasks/1
@api_view(["PUT"])
def update_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(
        task, data=request.data, partial=True
    )  # 'partial=True' for partial updates
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ex: DELETE /api/tasks/1
@api_view(["DELETE"])
def delete_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)

    task.delete()
    return Response(
        {"message": "Task deleted successfully."}, status=status.HTTP_204_NO_CONTENT
    )
