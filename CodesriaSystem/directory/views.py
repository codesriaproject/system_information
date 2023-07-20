from django.shortcuts import render
from django.views.generic import (
    ListView,CreateView,UpdateView,


)
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from directory.models import *
from django.urls import reverse_lazy
import random
from django.shortcuts import get_object_or_404, redirect, reverse

from directory.forms import *

# Create your views here.

#===========================================Start Status======================================

def add_status(request):
    return render(request,"pages/adminPage/status_form.html")

def add_status_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form=AddStatusForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            try:
                status=Status.objects.create(name=name)

                status.save()
                messages.success(request,"Successfully Added Status")
                return HttpResponseRedirect(reverse("add_status"))
            except:
                messages.error(request,"Failed to Add Status")
                return HttpResponseRedirect(reverse("add_status"))
        else:
            form=AddStatusForm(request.POST)
            return render(request, "pages/adminPage/status_form.html", {"form": form})

#========================================End Status==========================================
#========================================Start Directory=====================================


def add_directory(request):
    return render(request,"pages/adminPage/add_directory.html")

def add_directory_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form=AddDirectoryForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            surname=form.cleaned_data["surname"]
            countries=form.cleaned_data["countries"]
            gender=form.cleaned_data["gender"]
            email=form.cleaned_data["email"]
            phone_number=form.cleaned_data["phone_number"]
            biography=form.cleaned_data["biography"]
            bibliography=form.cleaned_data["bibliography"]
            orcid=form.cleaned_data["orcid"]
            affliation=form.cleaned_data["affliation"]
            status=form.cleaned_data["status"]
            try:
                directory=Directory.objects.create(
                    name=name,
                    surname=surname,
                    countries=countries,
                    gender=gender,
                    email=email,
                    phone_number=phone_number,
                    biography=biography,
                    bibliography=bibliography,
                    orcid=orcid,
                    affliation=affliation
  
                    )
                status_obj=Status.objects.get(id=status)
                directory.status_id=status_obj
                directory.save()
                messages.success(request,"Successfully Added In Directory")
                return HttpResponseRedirect(reverse("add_directory"))
            except Exception as e:
                messages.error(request,"Failed to Add In Directory" + str(e))
                return HttpResponseRedirect(reverse("add_directory"))
        else:
            form=AddDirectoryForm(request.POST)
            return render(request, "pages/adminPage/add_directory.html", {"form": form})


def list_directory(request):

    directory = Directory.objects.filter()

    context = {
        'directory': directory,

    }

    return render(request,"pages/adminPage/directory_list.html", context)


def directory_details(request,directory_id):
    directory=Directory.objects.get(id=directory_id)
    context={
        'directory':directory,
    }

    return render(request,"pages/adminPage/directory_details.html", context)
