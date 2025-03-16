from django.shortcuts import render
from itertools import chain

from .models import Tea, Equipment, Kit

def all_products(request):
    """A view to return all products page, including sorting and search queries"""

    teas = Tea.objects.all()
    equipment = Equipment.objects.all()
    kits = Kit.objects.all()

    all_products = list(chain(teas, equipment, kits))  # Merge all products into one list

    context = {
        'all_products': all_products,
    }

    return render(request, 'products/products.html', context)