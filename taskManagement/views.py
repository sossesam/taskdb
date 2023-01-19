from django.shortcuts import render,redirect
from .forms import TaskForm
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


def delete(request, list_id):
    item = taskD.objects.get(id=list_id)
    item.delete()
    messages.success(request, "item has been deleted")
    return redirect('home')
    

     
    