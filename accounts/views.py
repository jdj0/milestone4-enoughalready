from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserAccount
from .forms import UserAccountForm


def account(request):
    """ Display user account template """
    account = get_object_or_404(UserAccount, user=request.user)

    if request.method == 'POST':
        form = UserAccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Account has been updated')

    orders = account.orders.all()
    form = UserAccountForm(instance=account)

    template = 'accounts/account.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)
