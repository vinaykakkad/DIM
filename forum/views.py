from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.contrib import messages
from slugify import slugify

from .models import Post, Tags, Comment
from .forms import PostForm, CommentForm
from .utils import filter_posts


def post_list_view(request, *args, **kwargs):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            data = form.save(commit=False)
            data.slug = slugify(data.title)
            data.user = request.user
            data.save()
            form.save_m2m()
            return redirect("forum")

        messages.error(
            request, "There was some error while adding the post, please try again!!"
        )
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


def add_tag_view(request):
    if request.method == "POST":
        tag = None
        new_tag = request.POST.get("tag")

        try:
            tag = Tags.objects.get(tag=new_tag)
        except Exception as identifier:
            pass

        if tag is None:
            tag = Tags(tag=new_tag)
            tag.save()
            print("here")
            messages.success(request, "Tag added successfully")
            return redirect("add_tag")

        messages.error(request, "Try again")
        return redirect("forum")

    return redirect("forum")


def post_detail_view(request, slug, *args, **kwargs):
    post = Post.objects.get(slug=slug)
    comments = post.comments.all()
    comment_form = CommentForm()

    context = {"object": post, "comments": comments, "comment_form": comment_form}
    return render(request, "forum/post_detail.html", context)


def add_comment_view(request, post_pk):
    if request.method != "POST":
        messages.error(request, "You are not allowed to access this method")
        return redirect(request.META.get("HTTP_REFERER", "forum"))

    form = CommentForm(request.POST)

    if form.is_valid():
        data = form.save(commit=False)

        data.user = request.user
        data.post = Post.objects.get(pk=post_pk)

        data.save()
        return redirect(request.META.get("HTTP_REFERER", "forum"))

    messages.error(
        request, "There was some error while adding the comment, please try again!!"
    )
    return redirect(request.META.get("HTTP_REFERER", "forum"))
