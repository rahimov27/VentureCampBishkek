from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("Hello world")

def index(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about.html")

def blog(request):
    return render(request, "main/blog.html")

def contact(request):
    return render(request, "main/contact.html")

def project(request):
    return render(request, "main/project.html")

def service(request):
    return render(request, "main/service.html")

def single(request):
    return render(request, "main/single.html")












# def about(request):
#     return HttpResponse("About us")