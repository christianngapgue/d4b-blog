from django.urls import path

from blog.views import BlogListView

urlpatters = [
    path('', BlogListView.as_view(), name='home'),
]