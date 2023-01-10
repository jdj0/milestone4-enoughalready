

def bag_contents(request):

    bag_items = []
    total = 0
    item_count = 0

    context = {
        'bag_items': bag_items,
        'total': total,
        'item_count': item_count,
    }

    return context
