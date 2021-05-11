from django.shortcuts import render

# from account.models import Account


def home_page_view(request, *args, **kwargs):
    context = {}
    return render(request, "home/home.html", context)


# def leaderboard_view(request, *args, **kwargs):
#     # users = Account.objects.filter(is_superuser=False).order_by('-points','last_ans_time')
#     context = {'users': users}
#     return render(request, 'home/leaderboard.html', context)


def instruction_view(request, *args, **kwargs):
    context = {}
    return render(request, 'home/instructions.html', context)


def about_view(request, *args, **kwargs):
    context = {}
    return render(request, 'home/about.html', context)