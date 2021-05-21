from django.shortcuts import render
from .models import JobPost

def user_job_list_view(request):
	jobs = JobPost.objects.all()
	user_skills = request.user.skills.all()
	matched_jobs = list()

	for job in jobs:
		job_skills = job.skills.all()
		score = count()
