from django.shortcuts import render
# from summary.models import SumItems
from confirm.models import PSumItems
from twilio.rest import Client
from django.contrib.auth.models import User
from datetime import date


def myorders(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            orders1 = PSumItems.objects.all()
            status = request.POST.getlist('status')
            n = 0
            for st in orders1:
                stats = status[n]
                updte = PSumItems(id=st.id,
                                  user_name=st.user_name,
                                  pnumber=st.pnumber,
                                  selected_items=st.selected_items,
                                  items_cost=st.items_cost,
                                  items_weight=st.items_weight,
                                  items_price=st.items_price,
                                  total_cost=st.total_cost,
                                  date_created=st.date_created,
                                  status=stats)
                updte.save()
                n = n + 1
        orders = PSumItems.objects.all()
    else:
        # orders = SumItems.objects.filter(user_name=request.user)
        orders = PSumItems.objects.filter(user_name=request.user)

    order_date, idnum, username, status1 = [], [], [], []
    for x in orders:
        y = x.date_created
        ds = str(str(y))
        order_date.append(str(ds))
        idnum.append(str(x.id))
        username.append(x.user_name)
        status1.append(x.status)

    return render(request, 'myorders.html', {'order_date': order_date, 'id': idnum, 'username': username, 'status': status1})

