from django.urls import path
from .views import ContactUsPageView


urlpatterns = [
    path('', ContactUsPageView.as_view(), name='contactus_view')
]