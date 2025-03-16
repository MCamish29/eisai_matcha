from django.shortcuts import render
from .models import Tea, Equipment, Kit

def all_products(request):
    """A view to return all products page"""
    
    teas = Tea.objects.all()
    equipment = Equipment.objects.all()
    kits = Kit.objects.all()

    context = {
        'teas': teas,
        'equipment': equipment,
        'kits': kits,
    }

    return render(request, 'products/all_products.html', context)
