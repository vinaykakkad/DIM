from django.db.models.query_utils import Q
from .models import fields


def filter_courses(courses, request):
    filtered = False
    session = request.session

    # Clearing all filters
    try:
        if request.GET.get("clear") == "1":
            session["course_fields"] = None
            session["course_title"] = None
    except Exception as identifier:
        pass

    # If filters are receiced/valid, store them

    # fields
    try:
        f_fields = request.GET.getlist("fields")

        if f_fields is not None and len(f_fields) != 0:
            session["course_fields"] = f_fields
    except Exception as identifier:
        pass

    # title
    try:
        title = request.GET.get("title")

        if title is not None and title != "":
            session["course_title"] = title
    except Exception as identifier:
        pass

    # If session variables aren't initialized, initialize as None
    try:
        if session["course_fields"] is not None:
            pass
    except Exception as identifier:
        session["course_fields"] = None

    try:
        if session["course_title"] is not None:
            pass
    except Exception as identifier:
        session["course_title"] = None

    # Filtering data as per requirement

    # title
    if session["course_title"] is not None:
        filtered = True
        courses = courses.filter(name__icontains=session["course_title"])

    # fields
    if session["course_fields"] is not None:
        filtered = True
        received_fields = session["course_fields"]
        filter_fields = set(fields.objects.filter(Field__in=received_fields))
        final_courses = []

        for course in courses:
            if filter_fields.issubset(set(course.Field.all())):
                final_courses.append(course)

        courses = final_courses

    return courses, filtered
