from django.shortcuts import render, redirect

# Create your views here.

def view_cart(request):
    """A view that renders the shopping cart contents page"""
    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    """ Add a quantity of the specified product to the shopping cart """

    if request.method == "POST":
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})

        if str(product_id) in cart:
            cart[str(product_id)] += quantity
        else:
            cart[str(product_id)] = quantity

        request.session['cart'] = cart

        return redirect('view_cart')

    return redirect('products')