from django.shortcuts import render, get_object_or_404, redirect, reverse

from .cart import Cart
from .forms import AddToCartProductForm
from products.models import Product


def cart_detail_view(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})


def add_to_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    quantity_form = AddToCartProductForm(request.POST)

    if quantity_form.is_valid():
        cleaned_data = quantity_form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product, quantity)

        return redirect('cart:cart_detail')
