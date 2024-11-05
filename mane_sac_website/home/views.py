from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import UserCreationForm 

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
    return render(request, 'home/forum.html')