from django.shortcuts import render, redirect, reverse
from django.shortcuts import HttpResponse, get_object_or_404
from django.contrib import messages
from services.models import Service


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified service to the shopping bag """

    service = get_object_or_404(Service, pk=item_id)
    quantity = int(request.POST.get('quantity'))  # Service quantity in bag
    redirect_url = request.POST.get('redirect_url')  # Url redirect from bag

    size = None
    color = None
    webdev_options = None
    user_message = None

    if 'service_size' in request.POST:
        size = request.POST.get('service_size')
    if 'service_color' in request.POST:
        color = request.POST.get('service_color')
    if 'service_webdev_options' in request.POST:
        webdev_options = request.POST.get('service_webdev_options')
    if 'service_user_message' in request.POST:
        user_message = request.POST.get('service_user_message')

    bag = request.session.get('bag', {})  # Get or create bag in session

    # If size option is selected (Dimensions Dropdown)
    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id].keys():
                bag[item_id]['items_by_data'][size] += quantity
            else:
                bag[item_id]['items_by_data'][size] = quantity
        else:
            bag[item_id] = {'items_by_data': {size: quantity}}

    # if color option is selected (Color Scheme Dropdown)
    elif color:
        if item_id in list(bag.keys()):
            if color in bag[item_id].keys():
                bag[item_id]['items_by_data'] += quantity
            else:
                bag[item_id]['items_by_data'][color] = quantity
        else:
            bag[item_id] = {'items_by_data': {color: quantity}}

    # if webdev_options is selected (Webdev Options Checkbox)
    elif webdev_options:
        if item_id in list(bag.keys()):
            if webdev_options in bag[item_id].keys():
                bag[item_id]['items_by_data'][webdev_options] += quantity
            else:
                bag[item_id]['items_by_data'][webdev_options] = quantity
        else:
            bag[item_id] = {'items_by_data': {webdev_options: quantity}}

    # if message is selected (Service message text field)
    elif user_message:
        if item_id in list(bag.keys()):
            if user_message in bag[item_id].keys():
                bag[item_id]['items_by_data'][user_message] += quantity
            else:
                bag[item_id]['items_by_data'][user_message] = quantity
        else:
            bag[item_id] = {'items_by_data': {user_message: quantity}}

    # if only quantity is selected (default: 1)
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
