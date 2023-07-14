from django.urls import path
from .views import BlogsListView, BlogDetailsView
urlpatterns = [
    path("", BlogsListView.as_view(), name='blogs-list-view'),
    path("<str:slug>", BlogDetailsView.as_view(), name='blog-details-view'),
]