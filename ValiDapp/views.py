from django.shortcuts import render, redirect, HttpResponse
from .models import *

from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "add_virus.html")

def create_virus(request):
    errors = Viruses.objects.virus_validate(request.POST)
    
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    else:
        Viruses.objects.create(name=request.POST['name'], incubation_period=request.POST['incubation'], discovered=request.POST['discovered']) 
        return redirect('/allviruses')

def show_all(request):
    context = {
        "viruses": Viruses.objects.all()
    }
    return render(request, "all_viruses.html", context)