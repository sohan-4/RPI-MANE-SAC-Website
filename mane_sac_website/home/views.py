from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm 
import datetime

# Create your views here.

def home_view(request):
    events = event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'home/home.html', context)

def about_view(request):
    info = about.objects.all()
    context = {
        'info': info
    }
    return render(request, 'home/about.html', context)

def member_view(request):
    members = member.objects.all()
    context = {
        'members': members
    }
    return render(request, 'home/members.html', context)

def contact_view(request):
    contact_info = contact.objects.all()
    number = contact_info[0].phone
    number = str(number)
    number = number[2:]
    number = number[:3] + '-' + number[3:6] + '-' + number[6:]
    context = {
        'info': contact_info,
        'formatted_number': number
    }
    return render(request, 'home/contact.html', context)

def faq_view(request):
    questions = faq.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'home/faq.html', context)

def forum_view(request):
    posts = post.objects.all()
    context = {
        'posts': post
    }
    return render(request, 'home/forum.html')

def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        img = request.FILES.get('img')
        date_time = datetime.datetime.now()

        post = post.objects.create(title=title, text=text, img=img, date_time=date_time)
        post.save()
        print("hi", post)
        return redirect('forum_view')