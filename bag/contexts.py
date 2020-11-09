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
        if isinstance(item_data, int):
            service = get_object_or_404(Service, pk=item_id)
            total += item_data * service.price
            service_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'service': service,
            })
        else:
            service = get_object_or_404(Service, pk=item_id)
            for user_message, quantity in item_data['items_by_details'].items():
                total += quantity * service.price
                service_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'service': service,
                    'user_message': user_message,
                })

    if total > settings.TEN_OFF_THRESHOLD:
        """ 10% Off Promo using $500 as purchase threshold """

        # If order counts to the minimum amount in TEN_OFF_THRESHOLD
        # then user can get 10% off with STANDARD_PROMO_PERCENTAGE.
        # Decimal is prefered over Flow and
        # more accurate for financial transactions.
        promo = total * Decimal(settings.STANDARD_PROMO_PERCENTAGE / 100)
        ten_off_delta = settings.TEN_OFF_THRESHOLD - total

    else:
        promo = 0
        ten_off_delta =  settings.TEN_OFF_THRESHOLD - total

    grand_total = total - promo

    context = {
        'bag_items': bag_items,
        'total': total,
        'service_count': service_count,
        'promo': promo,
        'ten_off_delta': ten_off_delta,
        'ten_off_threshold': settings.TEN_OFF_THRESHOLD,
        'grand_total': grand_total,
    }

    print(f"promo is: {promo}")
    print(f"ten_off_delta: {ten_off_delta}")
    print(f"ten_off_threshold: {settings.TEN_OFF_THRESHOLD}")
    print(f"grand_total: {grand_total}")
    
    return context
