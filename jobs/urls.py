from django.urls import path

from .views import (
    user_job_list_view,
    recruiter_job_view,
    delete_job_post_view,
    matching_user_view,
)

urlpatterns = [
    path("jobs/", user_job_list_view, name="jobs"),
    path("recruiter/jobs/", recruiter_job_view, name="recruiter_jobs"),
    path("delete/job_post/", delete_job_post_view, name="job_post_delete"),
    path("jobs/<pk>/candidates/", matching_user_view, name="post_candidates")
    # path("add_comment/<int:post_pk>/", add_comment_view, name="add_comment"),
    # path("forum/<slug:slug>/", post_detail_view, name="post_detail"),
]
