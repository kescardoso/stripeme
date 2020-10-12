from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem

from services.models import Service

from bag.contexts import bag_contents


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('services'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HbQtKLzw1nOifV1h0UC0IaDughxZIEUKhV8GRaqF6JjR8OmxpMQfyatmo2dvQCSTunuRyGv1wDFuhzed7HxwqdQ0004tGcdn7',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
