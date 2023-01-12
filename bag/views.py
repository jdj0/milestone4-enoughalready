from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view thats shows all items added to the shopping bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ A view to... """

    return redirect(redirect_url)