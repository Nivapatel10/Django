from django.shortcuts import render
from todo.models import todo_task
def home(request):
    tasks = todo_task.objects.filter(is_completed = False)
    return render(request,"home.html")