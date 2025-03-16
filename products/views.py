from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Tea, Equipment, Kit, Category, Country

def all_products(request):
    """A view to return all products page"""
    
    teas = Tea.objects.all()
    equipment = Equipment.objects.all()
    kits = Kit.objects.all()
    search = None

    if request.GET:
        if 'q' in request.GET:
            search = request.GET['q']
            if not search:
                messages.error(request, "No search criteria entered!")
                return redirect(reverse('products'))
            
            # Perform search in category names, product names, and descriptions
            queries = Q(category__category__icontains=search) | Q(product_name__icontains=search) | Q(description__icontains=search)
            teas = teas.filter(queries)
            equipment = equipment.filter(queries)
            kits = kits.filter(queries)

    context = {
        'teas': teas,
        'equipment': equipment,
        'kits': kits,
        'search_term': search,
    }

    return render(request, 'products/all_products.html', context)


def tea(request):
    """A view to display tea products"""
    teas = Tea.objects.all()

    context = {
        'teas': teas,
    }

    return render(request, 'products/tea.html', context)


def equipment(request):
    """A view to display tea products"""
    equipment = Equipment.objects.all()

    context = {
        'equipment': equipment,
    }

    return render(request, 'products/equipment.html', context)


def kit(request):
    """A view to display tea products"""
    kits = Kit.objects.all()

    context = {
        'kits': kits,
    }

    return render(request, 'products/kits.html', context)