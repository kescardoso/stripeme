from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from services.models import Service


def bag_contents(request):

    bag_items = []
    total = 0
    grand_total = 0
    service_count = 0
    bag = request.session.get('bag', [])  # bag contents are an array

    for item in bag:
        """ View a list of items in bag """

        service = get_object_or_404(Service, pk=item["item_id"])
        total = service.price
        grand_total += total

        bag_items.append({
            'item_id': item["item_id"],
            'service': service,
            'color': item["color"] if 'color' in item else None,
            'size': item["size"] if 'size' in item else None,
            'user_message': item["user_message"] if 'user_message' in item else None,
        })

    if total < settings.TEN_OFF_THRESHOLD:
        """ 10% Off Promo using $500 as purchase threshold """

        # If order counts to the minimum amount in TEN_OFF_THRESHOLD
        # then user can get 10% off with STANDARD_PROMO_PERCENTAGE.
        # Decimal is prefered and more accurate for financial transactions.

        promo = grand_total * Decimal(settings.STANDARD_PROMO_PERCENTAGE / 100)
        ten_off_delta = settings.TEN_OFF_THRESHOLD - total

    else:
        promo = 0
        ten_off_delta = 0

    grand_total = promo + grand_total

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
