from django.shortcuts import render, redirect
from products.models import Products
from .models import SumItems
from datetime import date
from django.contrib import messages
from django.contrib.auth.models import User


def summary(request):
    user_name = request.user
    products = Products.objects.all()
    items = {}
    items_dict = {}
    selected_items, selected_weights, items_price, items_price1, items_price2, items_name, items_cost, items_weight = [], [], [], [], [], [], [], []
    selected_weights = request.POST.getlist('weights')
    selected_items = request.POST.getlist('items_sel')

    for r in products:
        items_price.append(r.product_price)
        items_name.append(r.product_name)

    items_price1 = items_price

    for key in items_name:
        for value in items_price:
            items_dict[key] = value
            items_price.remove(value)
            break

    for x in range(0, len(selected_weights)):
        y = selected_weights[x]
        if float(y) > 0:
            items_weight.append(float(y))

    for k in selected_items:
        items_price2.append(items_dict[k])

    for num1, num2 in zip(items_weight, items_price2):
        items_cost.append(float(num1) * float(num2))

    totcost = 0

    for tcost in items_cost:
        totcost = totcost + float(tcost)

    today = date.today()
    date_created = today.strftime('%Y-%m-%d')
    if not selected_items or totcost <= 0:
        messages.error(request, "Please select items by clicking on checkbox and select weight ")
        return redirect('produ')
    else:
        sumitems_obj = SumItems(user_name=user_name,  selected_items=selected_items, items_price=items_price2, items_weight=items_weight,
                                items_cost=items_cost,  total_cost=totcost, date_created=date_created)
        sumitems_obj.save()
    return render(request, 'summary.html', {'items': selected_items, 'aprices': items_price2, 'weights': items_weight,  'costs': items_cost, 'totcost': totcost, 'username': user_name})

