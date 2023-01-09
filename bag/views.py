from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ A view thats shows all items added to the shopping bag """

    return render(request, 'bag/bag.html')
