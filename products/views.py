from django.shortcuts import render, get_object_or_404
from .models import Item


def products(request):
    """ A view to show all products """

    context = {
        'items': Item.objects.all()
    }
    return render(request, 'products/products.html', context)


def product(request, item_id):
    """ A view to show a product's details """

    item = get_object_or_404(Item, pk=item_id)

    context = {
        'item': item,
    }

    return render(request, 'products/product.html', context)
