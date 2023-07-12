from django.shortcuts import render

def vigilhome(request):
    return render(request,"pages/vigilPage/index.html")


def vigil_profilview(request):

    return render(request,"pages/vigilPage/profil.html")