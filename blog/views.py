from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic.edit import DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import Blog, Comment
from .forms import BlogUpdateForm, BlogCreateForm, CommentForm, \
    CommentUpdateForm


def blog(request):
    """ A view that lists all blog posts """

    blogs = Blog.objects.all()
    context = {'blogs': blogs}

    return render(request, 'blog/blog.html', context)


def blog_post(request, pk):
    """ A view that shows the requested blog post and allows comments """

    blog = get_object_or_404(Blog, pk=pk)
    comments = blog.comment_set.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.published = timezone.now()
            comment.blog = blog
            comment.save()
            messages.success(request, 'Comment posted')
            return redirect('blog_post', pk=pk)
    else:
        form = CommentForm()
    context = {
        'blog': blog,
        'comments': comments,
        'form': form,
    }

    return render(request, 'blog/blog_post.html', context)


@staff_member_required
def blog_create(request):
    """ A view that allows staff to create blog posts  """

    form = BlogCreateForm(request.POST, request.FILES)

    if request.method == 'POST':
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.published = timezone.now()
            blog.image = request.FILES['image']
            blog.save()
            messages.success(request, 'Blog Published')
            return redirect('blog')

    context = {
        'form': form,
    }
    return render(request, 'blog/blog_create.html', context)


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
            messages.success(request, 'Blog Updated')
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


def comment_update(request, pk):
    """ A view that allows users to update their comments """

    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = CommentUpdateForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.published = timezone.now()
            comment.save()
            messages.success(request, 'Comment Updated')
            return redirect('blog_post', pk=comment.blog.pk)
    else:
        form = CommentForm(instance=comment)

    context = {
        'form': form,
        'comment': comment
    }

    return render(request, 'blog/comment_update.html', context)


class CommentDelete(DeleteView):
    model = Comment
    success_url = reverse_lazy('blog')
