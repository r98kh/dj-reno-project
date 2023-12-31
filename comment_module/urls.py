from django.urls import path
from .views import BlogPostDetailView

urlpatterns = [
    path('blog_post/<int:post_id>/', BlogPostDetailView.as_view(), name='blog_post_detail'),
]