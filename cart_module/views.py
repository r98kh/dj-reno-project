from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView

from cart_module.models import OrderDetail, Order
from product_module.models import Product


# Create your views here.

def add_product_to_order(request: HttpRequest):
    product_id = int(request.GET.get('product_id'))
    count = int(request.GET.get('count'))
    if count < 1:
        # count = 1
        return JsonResponse({
            'status': 'invalid_count',
            'text': 'مقدار وارد شده معتبر نمی باشد',
            'confirm_button_text': 'مرسی از شما',
            'icon': 'warning'
        })

    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_active=True, is_delete=False).first()
        if product is not None:
            current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
            current_order_detail = current_order.orderdetail_set.filter(product_id=product_id).first()
            if current_order_detail is not None:
                current_order_detail.count += count
                current_order_detail.save()
            else:
                new_detail = OrderDetail(order_id=current_order.id, product_id=product_id, count=count)
                new_detail.save()

            return JsonResponse({
                'status': 'success',
                'text': 'محصول مورد نظر با موفقیت به سبد خرید شما اضافه شد',
                'confirm_button_text': 'باشه ممنونم',
                'icon': 'success'
            })
        else:
            return JsonResponse({
                'status': 'not_found',
                'text': 'محصول مورد نظر یافت نشد',
                'confirm_button_text': 'مرسییییی',
                'icon': 'error'
            })
    else:
        return JsonResponse({
            'status': 'not_auth',
            'text': 'برای افزودن محصول به سبد خرید ابتدا می بایست وارد سایت شوید',
            'confirm_button_text': 'ورود به سایت',
            'icon': 'error'
        })


# class shoppingCart(ListView):
#     model = Order
#     template_name = 'cart_module/shopping_cart.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(shoppingCart, self).get_context_data(*args, **kwargs)
#         user_id = self.request.user.id
#
#         return context

def shopping_cart(request: HttpRequest):
    user_id = request.user.id
    try:
        user_order, created = Order.objects.get_or_create(user_id=user_id, is_paid=False)
        cart_detail, created = OrderDetail.objects.get_or_create(order_id=user_order.id).all()
        total = 0
        for i in cart_detail:
            total += i.get_total_price()
        context = {
            'orders': cart_detail,
            'total': total

        }
    except:
        context = {
            'orders': [],
            'total':0
        }
    return render(request, 'cart_module/shopping_cart.html', context)
