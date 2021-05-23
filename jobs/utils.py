from django.db.models.query_utils import Q
from .models import Skill


def filter_jobs(jobs, request):
    filtered = False
    session =  request.session

    # Clearing all filters
    try:
        if request.GET.get("clear") == "1":
            session["job_skills"] = None
            session["job_title"] = None
    except Exception as identifier:
        pass

    # If filters are receiced/valid, store them

    # skills
    try:
        skills = request.GET.getlist("skills")

        if (skills is not None and len(skills) != 0):
            session["job_skills"] = skills
    except Exception as identifier:
        pass

    # title
    try:
        title = request.GET.get("title")

        if title is not None and title != "":
            session["job_title"] = title
    except Exception as identifier:
        pass


    # If session variables aren't initialized, initialize as None
    try:
        if session["job_skills"] is not None:
            pass
    except Exception as identifier:
        session["job_skills"] = None
        
    try:
        if session["job_title"] is not None:
            pass
    except Exception as identifier:
        session["job_title"] = None

    # Filtering data as per requirement

    # title
    if session["job_title"] is not None:
        filtered = True
        jobs = jobs.filter(
            Q(role__icontains=session["job_title"]) |
            Q(company__icontains=session["job_title"])
        )

    # skills
    if session["job_skills"] is not None:
        filtered = True
        received_skills = session["job_skills"]
        filter_skills = set(Skill.objects.filter(skill__in=received_skills))
        final_jobs = []

        for job in jobs:
            if filter_skills.issubset(set(job.skills.all())):
                final_jobs.append(job)

        jobs = final_jobs


    return jobs, filtered