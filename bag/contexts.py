from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    item_count = 0
    delivery = 0
    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'item_count': item_count,
        'grand_total': grand_total,
    }

    return context
