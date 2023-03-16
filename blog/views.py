from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic.edit import DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from .models import Blog
from .forms import BlogUpdateForm


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


def blog_create(request):
    """ Comment """
    return render(request, 'blog/blog_create.html')


@staff_member_required
def blog_update(request, pk):
    """ A view that allows staff to update blog posts """

    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogUpdateForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.published = timezone.now()
            blog.save()
            return redirect('blog_post', pk=pk)
    else:
        form = BlogUpdateForm(instance=blog)
    context = {
        'form': form,
        'blog': blog
    }
    return render(request, 'blog/blog_update.html', context)


class BlogDelete(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog')
