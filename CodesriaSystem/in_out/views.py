from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from users.models import *
from in_out.models import *
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
# Create your views here.


def list_vigil_enter(request):

    user_vigil = CustomUser.objects.filter(user_type=2)

    context = {
        'user_vigil': user_vigil,

    }

    return render(request,"pages/vigilPage/enter.html", context)


def list_vigil_exit(request):

    user_vigil = CustomUser.objects.filter(user_type=2)

    context = {
        'user_vigil': user_vigil,

    }

    return render(request,"pages/vigilPage/exit.html", context)
