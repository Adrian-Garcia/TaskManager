from django.shortcuts import render
from .models import Task

# Create your views here.
class IndexView(generic.ListView):
    template_name = "tasks/index.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.all
    
