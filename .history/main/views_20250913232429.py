from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def index(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about.html")

def education(request):
    return render(request, "main/education.html")

def projects(request):
    return render(request, "main/projects.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"Message from {name} ({email}):\n\n{message}"
        
        send_mail(
            subject=f"New Contact Form Submission from {name}",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['your-email@gmail.com'],  # where you want to receive it
        )
        messages.success(request, 'Message sent successfully!')
    
    return render(request, 'contact.html')
