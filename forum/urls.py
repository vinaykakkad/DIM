from django.urls import path

from .views import post_list_view, post_detail_view

urlpatterns = [
    path("forum/", post_list_view, name="forum"),
    path("forum/<slug:slug>/", post_detail_view, name="post_detail"),
]
