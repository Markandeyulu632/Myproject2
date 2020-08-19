from django.shortcuts import render, redirect
from .models import Products
import numpy


def products(request):
    products = Products.objects.all()
    if request.method == 'POST':
        return redirect('home')
    else:
        n = []
        for i in numpy.arange(0.0, 50.0, 0.25):
            n.append(i)
    return render(request, 'products.html', {'products': products, 'nums': n})

