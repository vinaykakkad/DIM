from django.urls import path

from .views import (
    post_list_view,
    post_detail_view,
    add_tag_view,
    add_comment_view,
)

urlpatterns = [
    path("forum/", post_list_view, name="forum"),
    path("add_tag/", add_tag_view, name="add_tag"),
    path("add_comment/<int:post_pk>/", add_comment_view, name="add_comment"),
    path("forum/<slug:slug>/", post_detail_view, name="post_detail"),
]
