from django.db.models.query_utils import Q
from .models import Skill


def filter_events(events, request):
    filtered = False
    session = request.session

    # Clearing all filters
    try:
        if request.GET.get("clear") == "1":
            session["event_skills"] = None
            session["event_title"] = None
    except Exception as identifier:
        pass

    # If filters are receiced/valid, store them

    # skills
    try:
        skills = request.GET.getlist("skills")

        if skills is not None and len(skills) != 0:
            session["event_skills"] = skills
    except Exception as identifier:
        pass

    # title
    try:
        title = request.GET.get("title")

        if title is not None and title != "":
            session["event_title"] = title
    except Exception as identifier:
        pass

    # If session variables aren't initialized, initialize as None
    try:
        if session["event_skills"] is not None:
            pass
    except Exception as identifier:
        session["event_skills"] = None

    try:
        if session["event_title"] is not None:
            pass
    except Exception as identifier:
        session["event_title"] = None

    # Filtering data as per requirement

    # title
    if session["event_title"] is not None:
        filtered = True
        events = events.filter(Q(title__icontains=session["event_title"]))

    # skills
    if session["event_skills"] is not None:
        filtered = True
        received_skills = session["event_skills"]
        filter_skills = set(Skill.objects.filter(skill__in=received_skills))
        final_events = []

        for event in events:
            if filter_skills.issubset(set(event.skills.all())):
                final_events.append(event)

        events = final_events

    return events, filtered
