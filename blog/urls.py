from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogPostCreateView, BlogPostListView, BlogPostDetailView, BlogPostUpdateView, BlogPostDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('blogpost/create/', BlogPostCreateView.as_view(), name='blogpost_create'),
    path('blogposts', BlogPostListView.as_view(), name='blogposts'),
    path('blogpost/view/<int:pk>/', (BlogPostDetailView.as_view()), name='blogpost_view'),
    path('blogpost/edit/<int:pk>/', BlogPostUpdateView.as_view(), name='blogpost_edit'),
    path('blogpost/delete/<int:pk>/', BlogPostDeleteView.as_view(), name='blogpost_delete'),
]