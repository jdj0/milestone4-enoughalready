from django.urls import path
from . import views
from blog.views import BlogDelete, CommentDelete

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('blog_create/', views.blog_create, name='blog_create'),
    path('blog_post/<int:pk>/', views.blog_post, name='blog_post'),
    path('blog_update/<int:pk>/', views.blog_update, name='blog_update'),
    path('blog_delete/<int:pk>/', BlogDelete.as_view(), name='blog_delete'),
    path('comment_update/<int:pk>/', views.comment_update, name='comment_update'),
    path('comment_delete/<int:pk>/', CommentDelete.as_view(), name='comment_delete'),
]
