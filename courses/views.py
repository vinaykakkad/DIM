from django.shortcuts import render
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
        'page_data': courses,
        'fields': fields.objects.all(),
        'last_page': paginator.num_pages, 
        'filtered' : filtered
    }
    
    return render(request, 'courses/courses.html', context)