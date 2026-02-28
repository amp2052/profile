from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .middleware_utils import track_visit

@track_visit
def home(request):
    return render(request, 'app/home.html')

@track_visit
def skills(request):
    return render(request, 'app/skills.html')

@track_visit
def projects(request):
    return render(request, 'app/projects.html')

@track_visit
def education(request):
    return render(request, 'app/education.html')

@track_visit
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"New Contact Form Submission from {name}"
        full_message = f"Sender: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(
            subject,
            full_message,
            "amp2052@gmail.com",
            ["amp2052@gmail.com"],
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')

    return render(request, "app/contact.html")
