from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from services.models import Service


def bag_contents(request):

    bag_items = []
    total = 0
    service_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        """ View a list of items in bag """
        service = get_object_or_404(Service, pk=item_id)
        total += item_data * service.price
        service_count += item_data
        bag_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'service': service,
        })

    if total < settings.TEN_OFF_THRESHOLD:
        """ 10% Off Promo using $100 as purchase threshold """
        # If order counts to the minimum amount in TEN_OFF_THRESHOLD
        # then user can get 10% off with STANDARD_PROMO_PERCENTAGE.
        # Decimal is prefered and more accurate for financial transactions.

        promo = total * Decimal(settings.STANDARD_PROMO_PERCENTAGE / 100)
        ten_off_delta = settings.TEN_OFF_THRESHOLD - total
    else:
        promo = 0
        ten_off_delta = 0

    grand_total = promo + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'service_count': service_count,
        'promo': promo,
        'ten_off_delta': ten_off_delta,
        'ten_off_threshold': settings.TEN_OFF_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
