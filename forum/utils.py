from .models import Tags


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
    if request.session["title"] is not None:
        filtered = True
        filter_title = request.session["title"]
        posts = posts.filter(title__icontains=filter_title)

    if request.session["tags"] is not None:
        filtered = True
        received_tags = request.session["tags"]
        filter_tags = set(Tags.objects.filter(tag__in=received_tags))
        final_posts = []
        for post in posts:
            if filter_tags.issubset(set(post.tags.all())):
                final_posts.append(post)
        posts = final_posts


    return posts, filtered
