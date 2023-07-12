from django.shortcuts import render ,get_object_or_404, redirect, reverse
from users.models import *
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from users.forms import *


def adminhome(request):
    return render(request,"pages/adminPage/index.html")







def add_vigil(request):
    return render(request,"pages/adminPage/add_vigil.html")

def add_vigil_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form=AddVigilForm(request.POST,request.FILES)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            address=form.cleaned_data["address"]
            phone_number=form.cleaned_data["phone_number"]
            profile_pic=request.FILES['profile_pic']
            fs=FileSystemStorage()
            filename=fs.save(profile_pic.name,profile_pic)
            profile_pic_url=fs.url(filename)

            try:
                user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3)
                user.vigil.address=address
                user.vigil.phone_number=phone_number
                user.vigil.profile_pic=profile_pic_url
                user.save()
                messages.success(request,"Successfully Added Vigil")
                return HttpResponseRedirect(reverse("add_vigil"))
            except:
                messages.error(request,"Failed to Add Vigil")
                return HttpResponseRedirect(reverse("add_vigil"))
        else:
            form=AddVigilForm(request.POST)
            return render(request, "pages/adminPage/add_vigil.html", {"form": form})


#========================================END VIGIL=====================================================

#========================================START STAFF====================================================




def add_staff(request):
    return render(request,"pages/adminPage/add_staff.html")

def add_staff_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form=AddStaffForm(request.POST,request.FILES)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            address=form.cleaned_data["address"]
            phone_number=form.cleaned_data["phone_number"]
            nationality=form.cleaned_data["nationality"]
            status=form.cleaned_data["status"]
            salary=form.cleaned_data["salary"]
            department_id=form.cleaned_data["department"]
            profile_pic=request.FILES['profile_pic']
            gender=form.cleaned_data["gender"]
            fs=FileSystemStorage()
            filename=fs.save(profile_pic.name,profile_pic)
            profile_pic_url=fs.url(filename)

            try:
                user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
                user.staff.address=address
                department_obj=Department.objects.get(id=department_id)
                user.staff.departement_id=department_obj
                user.staff.phone_number=phone_number
                user.staff.nationality=nationality
                user.staff.status=status
                user.staff.salary=salary
                user.staff.gender=gender
                user.staff.profile_pic=profile_pic_url
                user.save()
                messages.success(request,"Successfully Added Staff")
                return HttpResponseRedirect(reverse("add_staff"))
            except:
                messages.error(request,"Failed to Add Staff")
                return HttpResponseRedirect(reverse("add_staff"))
        else:
            form=AddStaffForm(request.POST)
            return render(request, "pages/adminPage/add_staff.html", {"form": form})









def list_staff(request):

    staff = CustomUser.objects.filter(user_type=2)

    context = {
        'staff': staff,

    }

    return render(request,"pages/adminPage/staff_list.html", context)