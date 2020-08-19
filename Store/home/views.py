from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html', {})

