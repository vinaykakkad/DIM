from django.urls import path

from .views import (
    expert_event_list_view,
    event_post_view,
    delete_event_post_view,
    matching_expert_view,
)

urlpatterns = [
    path("events/", expert_event_list_view, name="events"),
    path("events/posts/", event_post_view, name="event_posts"),
    path("delete/event/post", delete_event_post_view, name="event_post_delete"),
    path("events/<pk>/candidates/", matching_expert_view, name="event_candidates"),
]
