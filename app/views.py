from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .middleware_utils import track_visit

# @track_visit
def home(request):
    return render(request, 'app/home.html')

# @track_visit
def skills(request):
    return render(request, 'app/skills.html')

# @track_visit
def projects(request):
    return render(request, 'app/projects.html')

# @track_visit
def education(request):
    return render(request, 'app/education.html')


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .middleware_utils import track_visit


# @track_visit
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        full_message = f"""
        Name: {name}
        Email: {email}

        Message:
        {message}
        """

        send_mail(
            subject="New Contact Form Message",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=["ampaws2052@gmail.com"],
        )

        messages.success(request, "Message sent successfully!")
        return redirect("contact")

    return render(request, "app/contact.html")