"""
URL configuration for reno project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_module.urls')),
    path('products/', include('product_module.urls')),
    path('accounts/', include('allauth.urls')),
    path('blogs/', include('blogs_module.urls')),
    path('contact-us/', include('contactus_module.urls')),
    path('about-us/', include('aboutus_module.urls')),
    path('order/', include('cart_module.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
