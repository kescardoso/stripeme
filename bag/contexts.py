from decimal import Decimal
from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    service_count = 0

    # 10% Off Promo
    if total < settings.TEN_OFF_THRESHOLD:
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
