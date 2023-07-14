from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blogs
class BlogDetailsView(DetailView):
    model = Blogs
    template_name = "blogs_module/blog_details.html"


class BlogsListView(ListView):
    model = Blogs
    template_name = "blogs_module/blogs_list.html"
