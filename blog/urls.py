from django.urls import path
from .views import BlogListView, BlogDetialView

app_name = "blog"
urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("post/<int:pk>/", BlogDetialView.as_view(), name="post_detail"),
]
