import json
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from users.EmailBackEnd import EmailBackEnd
from django.core.files.storage import FileSystemStorage

from users.models import *

from users.forms import *



#========================================Login Logout Start=====================================


def LoginPage(request):
    return render(request,"main/loginSite.html")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return redirect(reverse("admin_home"))
            elif user.user_type=="2":
                return redirect(reverse("staff_home"))
            elif user.user_type=="3":
                return redirect(reverse("vigil_home"))
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/log")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/log")



#========================================Login Logout End=====================================


#========================================Signature Start=====================================


def add_sign(request):

    return render(request, 'pages/add_signature.html')


def add_sign_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form = AddSignatureForm(request.POST, request.FILES)
        if form.is_valid():
            sign=form.cleaned_data["sign"]
            staff = get_object_or_404(Staff, admin_id=request.user.id)

            try:
                signature=Signature(staff_sign=staff,sign=sign)
                signature.save()
                messages.success(request,"Successfully Added In Sign")
                return HttpResponseRedirect(reverse("add_sign"))
            except Exception as e:
                messages.error(request,"Failed to Add In Signature" + str(e))
                return HttpResponseRedirect(reverse("add_sign"))
        else:
            form=AddSignatureForm(request.POST)
            return render(request, "pages/add_signature.html", {"form": form})



def sign_list(request):
    staff_instance = Staff.objects.get(admin_id=request.user)
    
    signature = Signature.objects.filter(staff_sign_id= staff_instance)

    context = {
        'signature': signature,

    }
    return render(request,"pages/signature.html", context)


#========================================Signature End=====================================


#========================================Departement Start=====================================


def add_department(request):
    return render(request,"pages/adminPage/add_departement.html")



def add_department_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form=AddDepartementForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            libelle=form.cleaned_data["libelle"]
            try:
                department=Department(name=name, libelle=libelle)
                department.save()
                messages.success(request,"Successfully Added In Department")
                return HttpResponseRedirect(reverse("add_department"))
            except Exception as e:
                messages.error(request,"Failed to Add In Department" + str(e))
                return HttpResponseRedirect(reverse("add_department"))
        else:
            form=AddDepartementForm(request.POST)
            return render(request, "pages/adminPage/add_departement.html", {"form": form})



def department_list(request):
    
    department = Department.objects.all()

    context = {
        'department': department,

    }
    return render(request,"pages/adminPage/departement_list.html", context)


#========================================Departement End=====================================
