from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.forms import UserCreationForm 
import datetime
from django.core.mail import EmailMessage
from django.conf import settings

def home_view(request):
    events = models.event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'home/home.html', context)

def about_view(request):
    info = models.about.objects.all()
    context = {
        'info': info
    }
    return render(request, 'home/about.html', context)

def member_view(request):
    members = models.member.objects.all()
    context = {
        'members': members
    }
    return render(request, 'home/members.html', context)

def contact_view(request):
    contact_info = models.contact.objects.all()
    context = {
        'info': contact_info,
    }
    return render(request, 'home/contact.html', context)

def faq_view(request):
    questions = models.faq.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'home/faq.html', context)

def forum_view(request):
    return render(request, 'home/forum.html')

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('content')
        img = request.FILES.get('img')
        major = request.POST.get('major')
        year = request.POST.get('year')
        email = request.POST.get('email')
        date_time = datetime.datetime.now()

        user_question = models.question.objects.create(
            title=title,
            text=text,
            img=img,
            date_time=date_time,
            major=major,
            year=year,
            email=email
        )
        user_question.save()

        message = (
            """A new question was asked on the MANE SAC website forum.
            Please also Remeber to check the admin page too!
            The title is: """ + title + """
            The text is: """ + text + """
            The major is: """ + (major if major else "No major was provided") + """
            The year is: """ + (year if year else "No year was provided") + """
            The email is: """ + email + """
            
            """
        )

        email_message = EmailMessage(
            subject=f"Question from Website - {title}",
            body=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=["biswas4@rpi.edu"],
        )

        if img:
            img.seek(0)
            email_message.attach(img.name, img.read(), img.content_type)

        email_message.send(fail_silently=False)

        return redirect('forum')