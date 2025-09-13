from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "about.html")

def education(request):
    return render(request, "main/education.html")

def projects(request):
    return render(request, "main/projects.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        send_mail(
            subject=f"Portfolio Contact from {name}",
            message=f"From: {email}\n\n{message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_EMAIL],
        )
        return redirect("home")

    return render(request, "contact.html")
