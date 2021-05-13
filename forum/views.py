from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator

from .models import Post, Tags


def post_list_view(request, *args, **kwargs):
    all_tags = Tags.objects.all()
    posts = Post.objects.order_by('title')
    filtered = False

    # Clearing all filters
    try:
        if request.GET.get('clear') == "1":
            request.session['tags'] = None
            request.session['title'] = None
    except Exception as identifier:
        pass

    # If filters are receiced/valid, store them
    try:
        if request.GET.getlist('tags') is not None and len(request.GET.getlist('tags')) != 0:
            request.session['tags'] = request.GET.getlist('tags')
    except Exception as identifier:
        pass

    try:
        if request.GET.get('title') is not None and request.GET.get('title') != "":
            request.session['title'] = request.GET.get('title')
    except Exception as identifier:
        pass

    # If session variables aren't initialized, initialize as None
    try:
        if request.session['tags'] is not None:
            pass
    except Exception as identifier:
        request.session['tags'] = None
    try:
        if request.session['title'] is not None:
            pass
    except Exception as identifier:
        request.session['title'] = None

    # Filtering data as per requirement
    if request.session['tags'] is not None:
        filtered = True
        received_tags = request.session['tags']
        filter_tags = set(Tags.objects.filter(tag__in=received_tags))
        final_posts = []
        for post in posts:
            if filter_tags.issubset(set(post.tags.all())):
                final_posts.append(post)
        posts = final_posts

    if request.session['title'] is not None:
        filtered = True
        filter_title = request.session['title']
        posts = posts.filter(title__icontains=filter_title)

    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {'page_data': posts, 'tags': all_tags,
               'filtered': filtered, 'last_page': paginator.num_pages}

    return render(request, 'forum/forum.html', context)

    # post_list = Post.objects.all()
    # paginator = Paginator(post_list, 1)

    # page = request.GET.get('page')
    # page_data = paginator.get_page(page)

    # context = {'page_data': page_data, 'last_page': paginator.num_pages}
    # return render(request, 'forum/forum.html', context)


def post_detail_view(request, slug, *args, **kwargs):
    post = Post.objects.get(slug=slug)

    context = {'object': post}
    return render(request, 'forum/post_detail.html', context)
