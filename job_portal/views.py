from django.shortcuts import render, get_object_or_404
from .models import Application, Company, Job, JobSeekerProfile, EmployerProfile, SavedJob


def home(request):
    return render(request, 'job_portal/home.html', {})


def job_list(request):
    jobs = Job.objects.select_related('company', 'job_category', 'location').all()
    return render(request, 'job_portal/job_list.html', {'jobs': jobs})


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'job_portal/job_detail.html', {'job': job})


def company_list(request):
    companies = Company.objects.all()
    return render(request, 'job_portal/company_list.html', {'companies': companies})


def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    return render(request, 'job_portal/company_detail.html', {'company': company})


def jobseeker_list(request):
    jobseekers = JobSeekerProfile.objects.select_related('user').all()
    return render(request, 'job_portal/jobseeker_list.html', {'jobseekers': jobseekers})


def employer_list(request):
    employers = EmployerProfile.objects.select_related('user').all()
    return render(request, 'job_portal/employer_list.html', {'employers': employers})


def application_list(request):
    applications = Application.objects.select_related('job', 'jobseeker_profile').all()
    return render(request, 'job_portal/application_list.html', {'applications': applications})


def saved_job_list(request):
    saved_jobs = SavedJob.objects.select_related('jobseeker_profile', 'job').all()
    return render(request, 'job_portal/saved_job_list.html', {'saved_jobs': saved_jobs})
