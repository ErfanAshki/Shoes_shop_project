from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import OrderForm
from .models import Order, OrderItem


@login_required
def order_create_view(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

    return render(request, 'orders/order.html')


