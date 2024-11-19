from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.forms import UserCreationForm 
import datetime

# Create your views here.

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

def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        img = request.FILES.get('img')
        date_time = datetime.datetime.now()

        question = question.objects.create(title=title, text=text, img=img, date_time=date_time)
        question.save()
        print("hi", question)
        return redirect('forum_view')