from django.shortcuts import render



def staffhome(request):
    return render(request,"pages/staffPage/index.html")


def staff_profilview(request):

    return render(request,"pages/staffPage/profil.html")