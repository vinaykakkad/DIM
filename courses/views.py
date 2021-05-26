from django.shortcuts import render
from .models import courses as crs
from django.core.paginator import Paginator, EmptyPage
# Create your views here.


def courses_views(request):
    courses_obj = crs.objects.all()
    
    courses = []
    for i in courses_obj:
        # print(i.Field.all())
        courses.append({"name":i.name, "price":i.price, "link":i.link, "field":i.Field})

    p = Paginator(courses, 10)

    page_num = request.GET.get('page', 1)

    try:
        courses = p.page(page_num)
    except EmptyPage:
        courses = p.page(1)
    
    return render(request, 'courses.html', {"courses":courses})