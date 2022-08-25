from django.shortcuts import render,redirect
from  .forms import TaskForm
from .models import taskD
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        
        if form.is_valid():
            form.save()
            all_task = taskD.objects.all()
            messages.success(request, ("new item as been added.."))
            return render(request, 'index.html', {"all_task":all_task})

    else:
         all_task = taskD.objects.all()
         return render(request, 'index.html', {"all_task":all_task})





     
    