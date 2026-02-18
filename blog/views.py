from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def resources(request):
    return render(request, "resources.html")

def posts(request):
    return render(request, "posts.html")

def about(request):
    return render(request, "about.html")
