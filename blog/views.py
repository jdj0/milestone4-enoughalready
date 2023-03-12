from django.shortcuts import render


def blog(request):
    """ A view that lists all blog posts """

    return render(request, 'blog/blog.html')
