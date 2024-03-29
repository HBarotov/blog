from django.urls import path
from .views import (
    BlogListView,
    BlogDetialView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

app_name = "blog"
urlpatterns = [
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    path("", BlogListView.as_view(), name="home"),
    path("post/<int:pk>/", BlogDetialView.as_view(), name="post_detail"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
]
