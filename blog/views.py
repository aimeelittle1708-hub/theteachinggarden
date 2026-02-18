from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm, ResourceForm
from .models import Resource


def home(request):
    return render(request, "home.html")


def resources(request):
    resources = Resource.objects.all()
    return render(request, "resources.html", {"resources": resources})


def posts(request):
    return render(request, "posts.html")


def about(request):
    return render(request, "about.html")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("home")

    return render(request, "auth/register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = LoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.cleaned_data["user"])
        return redirect("home")

    return render(request, "auth/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("home")


@login_required
def upload_resource(request):
    form = ResourceForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        resource = form.save(commit=False)
        resource.uploaded_by = request.user
        resource.save()
        return redirect("resources")

    return render(request, "upload.html", {"form": form})
