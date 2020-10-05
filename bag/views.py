from django.shortcuts import render, redirect, reverse
from django.shortcuts import HttpResponse, get_object_or_404
from django.contrib import messages
from services.models import Service


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add service options to the shopping bag """

    service = get_object_or_404(Service, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')  # Url redirect from bag
    bag = request.session.get('bag', {})  # Bag session + bag dictionary

    user_message = None
    if 'service_user_message' in request.POST:
        user_message = request.POST.get('service_user_message')

    if user_message:
        if item_id in list(bag.keys()):
            if user_message in bag[item_id]['items_by_details'].keys():
                bag[item_id]['items_by_details'][user_message] += quantity
            else:
                bag[item_id]['items_by_details'][user_message] = quantity
        else:
            bag[item_id] = {'items_by_details': {user_message: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {service.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of a service """

    service = get_object_or_404(Service, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    user_message = None
    if 'service_user_message' in request.POST:
        user_message = request.POST['service_user_message']
    bag = request.session.get('bag', {})

    if user_message:
        if quantity > 0:
            bag[item_id]['items_by_details'][user_message] = quantity
        else:
            del bag[item_id]['items_by_details'][user_message]
            if not bag[item_id]['items_by_details']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """

    try:
        user_message = None
        if 'service_user_message' in request.POST:
            user_message = request.POST['service_user_message']
        bag = request.session.get('bag', {})

        if user_message:
            del bag[item_id]['items_by_details'][user_message]
            if not bag[item_id]['items_by_details']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
