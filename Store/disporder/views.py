from django.shortcuts import render, redirect
from confirm.models import PSumItems


def disporder(request, my_id):

    if str(my_id[0:1]) == 'D':
        idn = int(str(my_id[1:]))
        # del_data = PSumItems(id=idn)
        PSumItems.objects.filter(id=idn).delete()
        return redirect('myorders')
    m_id = int(my_id)
    order = PSumItems.objects.get(id=m_id)
    s_items = order.selected_items
    li_items = s_items.strip("']['").split("', '")
    s_cost = order.items_cost
    li_cost = s_cost.strip("']['").split(',')
    s_price = order.items_price
    li_price = s_price.strip("']['").split(',')
    s_weight = order.items_weight
    li_weight = s_weight.strip("']['").split(',')
    total_cost = order.total_cost
    user_name = order.user_name
    status_s = order.status
    pnumber = order.pnumber

    return render(request, 'disporder.html', {'s_items': li_items, 's_cost': li_cost, 's_weight': li_weight,
                                              's_price': li_price, 'total_cost': total_cost, 'user_name': user_name,
                                              's_status': status_s, 's_pnumber': pnumber})
