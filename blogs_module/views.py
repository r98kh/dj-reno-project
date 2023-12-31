from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blogs
from comment_module.forms import CommentForm
from comment_module.models import Comments


class BlogDetailsView(DetailView):
    model = Blogs
    template_name = "blogs_module/blog_details.html"

    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetailsView, self).get_context_data(
            *args, **kwargs)
        comments = Comments.objects.filter(blog=self.object)
        context['comments'] = comments
        context['comment_form'] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = self.request.user
            comment.blog = self.get_object()
            comment.save()
        return self.get(request, *args, **kwargs)

class BlogsListView(ListView):
    model = Blogs
    template_name = "blogs_module/blogs_list.html"
    paginate_by = 10
