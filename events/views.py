from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from .models import EventPost, Skill
from .utils import filter_events
from .forms import EventPostForm
from account.models import Account


def expert_event_list_view(request):
    expert_skills = set(request.user.profile.skills.all())
    skills = Skill.objects.all()
    events = EventPost.objects.all()
    matched_events = list()

    # filtering events base on request
    events, filtered = filter_events(events, request)

    # filtering out events where no.of matches < 3
    for event in events:
        event_skills = set(event.skills.all())
        count = len(expert_skills.intersection(event_skills))

        if count > 0:
            matched_events.append(event)

    # pagination
    paginator = Paginator(matched_events, 5)
    page = request.GET.get("page")
    jobs = paginator.get_page(page)

    context = {
        "page_data": jobs,
        "skills": skills,
        "filtered": False,
        "last_page": paginator.num_pages,
    }

    return render(request, "events/event_list.html", context)


def event_post_view(request):
    if request.method == "POST":
        form = EventPostForm(request.POST)

        if form.is_valid():
            data = form.save(commit=False)
            data.posted_by = request.user

            data.save()
            form.save_m2m()

            return redirect("event_posts")

        messages.error(
            request, "There was some error while posting the event, please try again!!"
        )
        return redirect("event_posts")

    events = request.user.event_posts.all()
    form = EventPostForm()

    context = {"events": events, "form": form}

    return render(request, "events/event_posts.html", context)


def delete_event_post_view(request):
    event_pk = request.POST.get("event_pk")
    EventPost.objects.get(pk=event_pk).delete()

    return redirect("event_posts")


def matching_expert_view(request, pk):
    event_skills = set(EventPost.objects.get(pk=pk).skills.all())
    experts = Account.objects.filter(type="expert")

    matching_expert = list()

    for expert in experts:
        try:
            expert_skills = set(expert.profile.skills.all())
        except Exception as identifier:
            continue

        count = len(expert_skills.intersection(event_skills))

        if count > 0:
            matching_expert.append(expert)

    context = {"experts": matching_expert}

    return render(request, "events/event_candidates.html", context)
