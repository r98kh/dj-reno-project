from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.template.loader import render_to_string
from cart_module.models import OrderDetail, Order
from product_module.models import Product
from django.views.generic.base import View
from user_module import forms,models
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.urls import reverse


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

@login_required
def shopping_cart(request: HttpRequest):
    user_id = request.user.id
    detail_id = request.GET.get('detail_id')
    quantity = request.GET.get('quantity')

    if quantity and int(quantity) > 0:
        order_detail = OrderDetail.objects.filter(id=detail_id).first()
        order_detail.count = quantity
        order_detail.save()

    elif detail_id:
        OrderDetail.objects.filter(id=detail_id, order__is_paid=False,
                                                            order__user_id=request.user.id).delete()

    try:
        user_order, created = Order.objects.get_or_create(user_id=user_id, is_paid=False)
        # print(user_order)
        # cart_detail, created = OrderDetail.objects.get_or_create(order_id=user_order.id)
        cart_detail = OrderDetail.objects.filter(order_id=user_order.id).all()
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

@method_decorator(login_required, name='dispatch')
class checkoutView(View):
    def get(self, request):
        
        
        billingdetails = models.BillingDetails.objects.filter(user_id=request.user.id).first()
        user = models.CustomUser.objects.filter(id=request.user.id).first()
        user_form = forms.UserForm(instance=user)
        billingdetails_form = forms.BillingDetailsForm(instance=billingdetails)
        user_order, created = Order.objects.get_or_create(user_id=request.user.id, is_paid=False)

        order_detail = OrderDetail.objects.filter(order_id=user_order)
        total = 0
        for i in order_detail:
            total += i.get_total_price()
        context = {
            'order_detail':order_detail,
            'total': total,
            'user_form': user_form,
            'billingdetails_form': billingdetails_form,
        }

        return render(request, 'cart_module/checkout.html', context)
        

    def post(self, request):
        billingdetails, created = models.BillingDetails.objects.get_or_create(user_id=request.user.id)
        user = models.CustomUser.objects.filter(id=request.user.id).first()
        order_detail = OrderDetail.objects.filter(order__user_id=request.user.id)

        user_form = forms.UserForm(request.POST, request.FILES,instance=user)
        billingdetails_form = forms.BillingDetailsForm(request.POST, request.FILES,instance=billingdetails)

        if billingdetails_form.is_valid() and user_form.is_valid():
            user_form.save(commit=True)
            billingdetails_form.save(commit=False)
            billingdetails_form.user = request.user
            billingdetails_form.save(commit=True)
            
            current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
            for detail in order_detail:
                detail.product.quantity_sold += 1
                detail.product.save()
                detail.final_price = detail.product.price
                detail.save()
            current_order.is_paid = True
            current_order.payment_data = '2022-06-04'
            current_order.save()

            return render(request, 'cart_module/success.html')
        
        order_detail = OrderDetail.objects.filter(order__user_id=request.user.id)
        total = 0
        for i in order_detail:
            total += i.get_total_price()
        context = {
            'order_detail':order_detail,
            'total': total,
            'user_form': user_form,
            'billingdetails_form': billingdetails_form,
        }
        return render(request, 'cart_module/checkout.html', context)