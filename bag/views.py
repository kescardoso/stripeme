from django.shortcuts import render, redirect, reverse
from django.shortcuts import HttpResponse, get_object_or_404
from django.contrib import messages
from services.models import Service


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    service = get_object_or_404(Service, pk=item_id)
    quantity = int(request.POST.get('quantity'))  # Service quantity in bag
    redirect_url = request.POST.get('redirect_url')  # Url redirect from bag
    bag = request.session.get('bag', {})  # Bag content is stored in session

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request, f'Updated {service.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {service.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)
