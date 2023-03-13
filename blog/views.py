from django.shortcuts import render, get_object_or_404
from .models import Blog


def blog(request):
    """ A view that lists all blog posts """

    blogs = Blog.objects.all()
    context = {'blogs': blogs}

    return render(request, 'blog/blog.html', context)


def blog_post(request, pk):
    """ A view that shows the requested blog post """

    blog = get_object_or_404(Blog, pk=pk)
    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog_post.html', context)
