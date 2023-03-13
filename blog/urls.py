from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('blog_post/<int:pk>/', views.blog_post, name='blog_post'),
]
