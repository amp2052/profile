from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'app/home.html')

def skills(request):
    return render(request, 'app/skills.html')

def projects(request):
    return render(request, 'app/projects.html')

def education(request):
    return render(request, 'app/education.html')
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

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
            "amp2052@gmail.com",        # sender
            ["amp2052@gmail.com"],      # recipient(s) -> must be a list
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')

    return render(request, "app/contact.html")
