from django.shortcuts import render

# Create your views here.

def testindex(request):
    return render(request,"pages/index.html")