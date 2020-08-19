from django.shortcuts import render
from summary.models import SumItems
from .models import PSumItems
from register.forms import UserRegisterForm
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
import os
import smtplib
from email.message import EmailMessage
from mystore.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD


def confirm(request):
    username = request.POST.get('username')
    items = SumItems.objects.filter(user_name=username).latest('id')
    sel_items = items.selected_items
    sel_costs = items.items_cost
    sel_weights = items.items_weight
    sel_prices = items.items_price
    sel_total_costs = items.total_cost
    sel_date_creates = items.date_created

    Eobj = User.objects.get(username=username)
    email = Eobj.email

    confirm_data = PSumItems(user_name=username, selected_items=sel_items, items_cost=sel_costs, items_weight=sel_weights, items_price=sel_prices, total_cost=sel_total_costs, date_created=sel_date_creates)
    confirm_data.save()
    temp_data = SumItems.objects.all().delete()

    # msg = EmailMessage()
    # msg['subject'] = 'Your order details with Mystore'
    # msg['From'] = EMAIL_HOST_USER
    # msg['To'] = email
    # msg.set_content('Here is your order details')
    #
    # # with open('Mywife.jpg', 'rb') as f:
    # #     file_data = f.read()
    # #     file_name = f.name
    # # msg.add_attachment('file_data', subtype='', filename=file_name)
    #
    # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    #     smtp.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    #     smtp.send_messa       subject = 'Welcome to Murugan Yoga Center'

    subject = 'Welcome to Mystore'
    message = 'Hi ,\n' \
              ' This is your order'

    recepient = str(email)
    # mail = EmailMessage(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
    # mail.attach('Mywife.png', img_data, 'image/png')
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)

    # mail.attach('Mywife.png', img_data, 'image/png')
    # mail.send()

    return render(request, 'confirm.html', {})
