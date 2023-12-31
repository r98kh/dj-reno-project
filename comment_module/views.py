from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comments
from .forms import CommentForm
from product_module.models import Product

class BlogPostDetailView(LoginRequiredMixin, View):
    template_name = 'product_module/product_details.html'
    login_url = '/accounts/login/'  # اگر کاربر وارد نشده باشد به این آدرس هدایت می‌شود

    def get(self, request, Product_id):
        product = get_object_or_404(Product, id=Product_id)
        comments = Comments.objects.filter(product_id=Product_id)
        form = CommentForm()
        return render(request, self.template_name, {'post': product, 'comments': comments, 'form': form})

    def post(self, request, Product_id):
        post = get_object_or_404(Product, id=Product_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.product = Product_id
            comment.save()
            form = CommentForm()
        comments = Comments.objects.filter(product_id=Product_id)
        return render(request, self.template_name, {'post': post, 'comments': comments, 'form': form})
