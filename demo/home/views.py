from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"home/index6.html",{})

def segundo(request):
    return render(request,"home/index2-1.html",{})
