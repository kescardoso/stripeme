from django.shortcuts import render, redirect, reverse
from django.shortcuts import HttpResponse, get_object_or_404
from django.contrib import messages
from services.models import Service


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add service options to the shopping bag """
    
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

    bag = request.session.get('bag', [])  # Get or create bag in session
    temp_item = {}
    temp_item["item_id"] = item_id

    # If size option is selected (Dimensions Dropdown)
    if size:
        temp_item["size"] = size

    # if color option is selected (Color Scheme Dropdown)
    if color:
        temp_item["color"] = color

    # if webdev_options is selected (Webdev Options Checkbox)
    if webdev_options:
        temp_item["webdev_options"] = webdev_options

    # if message is selected (Service message text field)
    if user_message:
        temp_item["user_message"] = user_message

    bag.append(temp_item)

    request.session['bag'] = bag
    return redirect(redirect_url)
