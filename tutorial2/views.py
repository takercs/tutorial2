from django.shortcuts import render

# Create your views here.

def about(request):

    return render(request, "about.html", {})

def work(request):

    return render(request,"work.html",{})

def cover(request):

    return render(request,"cover.html",{})
