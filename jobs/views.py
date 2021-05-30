from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from .models import JobPost, Skill
from .utils import filter_jobs
from .forms import JobPostForm
from account.models import Account


def user_job_list_view(request):
    user_skills = set(request.user.profile.skills.all())
    skills = Skill.objects.all()
    jobs = JobPost.objects.all()
    matched_jobs = list()

    # filtering jobs based on request
    jobs, filtered = filter_jobs(jobs, request)

    # filtering out jobs where no. of matches < 3
    for job in jobs:
        job_skills = set(job.skills.all())
        count = len(user_skills.intersection(job_skills))

        if count > 0:
            matched_jobs.append(job)

    # pagination
    paginator = Paginator(matched_jobs, 5)
    page = request.GET.get("page")
    jobs = paginator.get_page(page)

    context = {
        "page_data": jobs,
        "skills": skills,
        "filtered": filtered,
        "last_page": paginator.num_pages,
    }

    return render(request, "jobs/job_list.html", context)


def recruiter_job_view(request, *args, **kwargs):
    if request.method == "POST":
        form = JobPostForm(request.POST)

        if form.is_valid():
            data = form.save(commit=False)
            data.recruiter = request.user

            data.save()
            form.save_m2m()

            return redirect("recruiter_jobs")

        messages.error(
            request, "There was some error while posting the job, please try again!!"
        )
        return redirect("recruiter_jobs")

    jobs = request.user.job_posts.all()
    form = JobPostForm()

    context = {"jobs": jobs, "form": form}

    return render(request, "jobs/recruiter_jobs.html", context)


def delete_job_post_view(request):
    post_pk = request.POST.get("post_pk")
    JobPost.objects.get(pk=post_pk).delete()

    return redirect("recruiter_jobs")


def matching_user_view(request, pk):
    job_skills = set(JobPost.objects.get(pk=pk).skills.all())
    users = Account.objects.all()

    matching_user = list()

    for user in users:
        try:
            user_skills = set(user.profile.skills.all())
        except Exception as identifier:
            continue

        count = len(user_skills.intersection(job_skills))

        if count > 0:
            matching_user.append(user)

    context = {"users": matching_user}

    return render(request, "jobs/post_candidates.html", context)
