from django.shortcuts import render, redirect
from . forms import UserRegisterForm
from mystore.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
# from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # user = form.save()
            # user.refresh_from_db()
            # phone = form.cleaned_data.get('pnumber')
            # user.Meta.pnumber = phone
            # user.save()

            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            phone = form.cleaned_data.get('pnumber')
            email = form.cleaned_data.get('email')
            address = form.cleaned_data.get('address')

            subject = 'Welcome to Mystore'
            message = 'Hi ,\n' \
                      ' This is to confirm your registration with us.' \
                      '\n Your userid is : ' + username + ' .' \
                      '\n Thank you  \n  Mystore'

            recepient = str(email)
            send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
            return render(request, 'regconfirm.html', {'last_name': last_name, 'username': username})
    else:
        form = UserRegisterForm
    return render(request, 'register.html', {'form': form})

