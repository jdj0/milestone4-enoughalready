from products.models import Item
from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def view_bag(request):
    """ A view thats shows all items added to the shopping bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ A view to add the item to the shopping bag """

    item = Item.objects.get(pk=item_id)
    item_quantity = item.quantity
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    bag[item_id] = item_quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)