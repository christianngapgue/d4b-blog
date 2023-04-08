from django.urls import path

from blog.views import BlogCreateView, BlogDetailView, BlogListView

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', BlogCreateView.as_view(), name="post_new"),
    path('', BlogListView.as_view(), name='home'),
]