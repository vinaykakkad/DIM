from django.shortcuts import render

# from account.models import Account


def home_page_view(request, *args, **kwargs):
    context = {}
    return render(request, "home/home.html", context)