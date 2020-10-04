from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from services.models import Service


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add service options to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')  # Url redirect from bag
    bag = request.session.get('bag', {})

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
    # else:
    #     if item_id in list(bag.keys()):
    #         bag[item_id] += quantity
    #     else:
    #         bag[item_id] = quantity

    request.session['bag'] = bag
    print()
    return redirect(redirect_url)


# def remove_from_bag(request, item_id):
#     """ Remove specific services from the shopping bag """

#     user_message = None
#     if 'service_user_message' in request.POST:
#         user_message = request.POST.get('service_user_message')

#     bag = request.session.get('bag', [])

#     if user_message:
#         del bag[item_id][user_message]
#         if not bag[item_id]:
#             bag.pop(item_id)
#     else:
#         bag.pop(item_id)

#     request.session['bag'] = bag
#     return HttpResponse(status=200)
