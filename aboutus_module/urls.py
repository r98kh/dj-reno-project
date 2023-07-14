from django.urls import path
from .views import AboutUsPageView


urlpatterns =[
    path('', AboutUsPageView.as_view(), name='aboutus_view'),
]