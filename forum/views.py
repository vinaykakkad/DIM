from django.shortcuts import redirect, render
from django.views import View
from django.core.paginator import Paginator
from slugify import slugify


from .models import Post, Tags, PostForm


def filter_posts(posts, request):
    filtered = False

    # Clearing all filters
    try:
        if request.GET.get("clear") == "1":
            request.session["tags"] = None
            request.session["title"] = None
    except Exception as identifier:
        pass

    # If filters are receiced/valid, store them
    try:
        if (
            request.GET.getlist("tags") is not None
            and len(request.GET.getlist("tags")) != 0
        ):
            request.session["tags"] = request.GET.getlist("tags")
    except Exception as identifier:
        pass

    try:
        if request.GET.get("title") is not None and request.GET.get("title") != "":
            request.session["title"] = request.GET.get("title")
    except Exception as identifier:
        pass

    # If session variables aren't initialized, initialize as None
    try:
        if request.session["tags"] is not None:
            pass
    except Exception as identifier:
        request.session["tags"] = None
    try:
        if request.session["title"] is not None:
            pass
    except Exception as identifier:
        request.session["title"] = None

    # Filtering data as per requirement
    if request.session["tags"] is not None:
        filtered = True
        received_tags = request.session["tags"]
        filter_tags = set(Tags.objects.filter(tag__in=received_tags))
        final_posts = []
        for post in posts:
            if filter_tags.issubset(set(post.tags.all())):
                final_posts.append(post)
        posts = final_posts

    if request.session["title"] is not None:
        filtered = True
        filter_title = request.session["title"]
        posts = posts.filter(title__icontains=filter_title)

    return posts, filtered


def post_list_view(request, *args, **kwargs):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            print("here")
            data = form.save(commit=False)
            data.slug = slugify(data.title)
            data.save()
            form.save_m2m()
            return redirect("forum")

    all_tags = Tags.objects.all()
    posts = Post.objects.order_by("title")
    form = PostForm()

    posts, filtered = filter_posts(posts, request)

    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    posts = paginator.get_page(page)

    context = {
        "page_data": posts,
        "tags": all_tags,
        "form": form,
        "filtered": filtered,
        "last_page": paginator.num_pages,
    }

    return render(request, "forum/forum.html", context)


def post_detail_view(request, slug, *args, **kwargs):
    post = Post.objects.get(slug=slug)

    context = {"object": post}
    return render(request, "forum/post_detail.html", context)
