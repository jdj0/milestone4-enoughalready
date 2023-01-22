from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Item

# Create your views here.


def view_bag(request):
    """ A view thats shows all items added to the shopping bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ A view to add the item to the shopping bag """

    item = get_object_or_404(Item, pk=item_id)
    item_quantity = item.quantity
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    bag[item_id] = item_quantity
    messages.success(request, f'Added "{item.title}" to your bag')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        item = get_object_or_404(Item, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed "{item.title}" from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)