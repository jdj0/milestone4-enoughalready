from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Item


def bag_contents(request):

    bag_items = []
    total = 0
    item_count = 0
    delivery = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        item = get_object_or_404(Item, pk=item_id)
        total += quantity * item.price
        item_count += quantity
        bag_items.append({
            'item:id': item_id,
            'quantity': quantity,
            'item': item,
        })

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'item_count': item_count,
        'grand_total': grand_total,
    }

    return context
