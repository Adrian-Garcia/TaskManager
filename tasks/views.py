from django.shortcuts import render
from .models import Task
from django.views import generic
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
class IndexView(generic.ListView):
    template_name = "tasks/index.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.all

def detail(request: WSGIRequest, task_id: int) -> HttpResponse:
    task = get_object_or_404(Task, pk=task_id)
    return render(
        request,
        "tasks/detail.html",
        {"task":task}
    )

