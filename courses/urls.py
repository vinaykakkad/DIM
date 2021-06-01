from django.urls import path

from .views import temp_add, courses_views

urlpatterns = [
    path("courses/", courses_views, name="courses"),
    path("temp_add/", temp_add),
]
