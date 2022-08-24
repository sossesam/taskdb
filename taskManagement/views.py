from django.shortcuts import render
from .models import taskD

# Create your views here.

def home(request):

    all_task = taskD.objects.all()

    return render(request, 'index.html', {"all_task":all_task})