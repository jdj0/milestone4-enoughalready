from django.shortcuts import render, redirect, reverse, \
    get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import OrderLineItem, Order
from products.models import Item
from accounts.models import UserAccount
from accounts.forms import UserAccountForm
from bag.contexts import bag_contents

import json
import stripe


@require_POST
def cache_checkout_data(request):
    """ Handles the caching of checkout data entered by user """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, there has been an error \
            with your payment. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """ Using bag items, customer info and stripe, creates an order """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, quantity in bag.items():
                try:
                    item = Item.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        item=item,
                        quantity=quantity,
                        )
                    order_line_item.save()
                except Item.DoesNotExist:
                    messages.error(request, (
                        "We couldn't find one of your items in our database. "
                        "Please get in touch so we can help!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            # Decrease item quantities
            for item_id, quantity in bag.items():
                try:
                    item = Item.objects.get(id=item_id)
                    item.quantity -= quantity
                    item.save()
                except Item.DoesNotExist:
                    messages.error(request, (
                        "We couldn't find one of your items in our database. "
                        "Please get in touch so we can help!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            # Save customer info
            request.session['save_info'] = 'save-info' in request.POST
            # Redirect to success page
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, 'There is an error with the form. \
                Please check your info.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There is nothing in your bag... yet!")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                account = UserAccount.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': account.user.get_full_name(),
                    'email': account.user.email,
                    'phone_number': account.default_phone_number,
                    'country': account.default_country,
                    'postcode': account.default_postcode,
                    'town_or_city': account.default_town_or_city,
                    'street_address1': account.default_street_address1,
                    'street_address2': account.default_street_address2,
                    'county': account.default_county,
                })
            except UserAccount.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key not found. \
            Is it set in the enviroment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """ Process for a successful checkout """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    # connects user to order and saves user info
    if request.user.is_authenticated:
        account = UserAccount.objects.get(user=request.user)
        order.user_account = account
        order.save()

        if save_info:
            account_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_account_form = UserAccountForm(account_data, instance=account)
            if user_account_form.is_valid():
                user_account_form.save()

    messages.success(request, f'Order Successful! \
        Your order number is {order_number}. \
        Your order confirmation will be sent to {order.email}')
    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
