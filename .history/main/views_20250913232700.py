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
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and message:
            full_message = f"Message from {name} ({email}):\n\n{message}"
            
            try:
                send_mail(
                    subject=f"New Contact Form Submission from {name}",
                    message=full_message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=['your-email@gmail.com'],  # Replace with your actual email
                    fail_silently=False,
                )
                messages.success(request, 'Message sent successfully!')
                return redirect('contact')  # Redirect to avoid resubmission on page refresh
            except Exception as e:
                messages.error(request, f"Error sending message: {e}")
        else:
            messages.warning(request, "Please fill in all fields.")

    return render(request, 'main/contact.html')
