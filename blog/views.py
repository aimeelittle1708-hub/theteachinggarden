from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.db.models import Q

from .forms import RegisterForm, LoginForm, ResourceForm
from .models import Resource


def home(request):
    return render(request, "home.html")


def resources(request):
    resources = Resource.objects.all()

    subject = request.GET.get("subject")
    year = request.GET.get("year")
    query = request.GET.get("q")

    if subject:
        resources = resources.filter(subject=subject)

    if year:
        resources = resources.filter(year_group=year)

    if query:
        resources = resources.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    context = {
        "resources": resources,
        "selected_subject": subject,
        "selected_year": year,
        "query": query,
    }

    return render(request, "resources.html", context)


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


@login_required
def edit_resource(request, pk):
    resource = get_object_or_404(Resource, pk=pk)

    if resource.uploaded_by != request.user:
        return HttpResponseForbidden("You are not allowed to edit this resource.")

    form = ResourceForm(request.POST or None, request.FILES or None, instance=resource)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("resources")

    return render(request, "edit_resource.html", {"form": form, "resource": resource})


@login_required
def delete_resource(request, pk):
    resource = get_object_or_404(Resource, pk=pk)

    if resource.uploaded_by != request.user:
        return HttpResponseForbidden("You are not allowed to delete this resource.")

    if request.method == "POST":
        # Try to delete the Cloudinary asset too
        try:
            resource.file.delete()
        except Exception:
            pass

        resource.delete()
        return redirect("resources")

    return render(request, "confirm_delete.html", {"resource": resource})
