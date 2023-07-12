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