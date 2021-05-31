import csv
import os
from django.http.request import HttpRequest
from django.http.response import Http404

from django.shortcuts import redirect, render
from django.core.paginator import Paginator

from .models import courses as crs, fields
from .utils import filter_courses


def courses_views(request):
    courses = crs.objects.all()

    courses, filtered = filter_courses(courses, request)

    paginator = Paginator(courses, 10)
    page = request.GET.get("page")
    courses = paginator.get_page(page)

    context = {
        "page_data": courses,
        "fields": fields.objects.all(),
        "last_page": paginator.num_pages,
        "filtered": filtered,
    }

    return render(request, "courses/courses.html", context)


def temp_add(request):
    print(os.getcwd())
    with open('courses/courses.csv') as csv_file:

        courses = csv.reader(csv_file)
        count = 0

        for row in courses:
            count += 1

            if count == 1:
                continue


            current_field = None
            current_course = None

            try:
                current_course = crs.objects.get(name=row[0])
            except Exception as e:
                pass

            if current_course is not None:
                continue

            try:
                current_field = fields.objects.get(Field=row[4])
            except Exception as e:
                pass

            if current_field is None:
                current_field = fields(Field=row[4])
                current_field.save()

            new_course = crs(
                name=row[0],
                link=row[1],
                price=int(row[2][2:]),
                description=row[3],
            )
            new_course.save()
            new_course.Field.add(current_field)

    return redirect('home')