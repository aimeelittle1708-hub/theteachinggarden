from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def about(request):
    form = ContactForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        messages.success(request, "Thanks! Your message has been received.")
        return redirect("about")

    return render(request, "about/about.html", {"form": form})