from django.shortcuts import render


def account(request):
    """ Display user account template """
    template = 'accounts/account.html'
    context = {}

    return render(request, template, context)
