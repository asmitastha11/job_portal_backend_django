from django.urls import path
from . import views

app_name = 'job_portal'

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/<int:pk>/', views.job_detail, name='job_detail'),
    path('companies/', views.company_list, name='company_list'),
    path('companies/<int:pk>/', views.company_detail, name='company_detail'),
    path('jobseekers/', views.jobseeker_list, name='jobseeker_list'),
    path('employers/', views.employer_list, name='employer_list'),
    path('applications/', views.application_list, name='application_list'),
    path('saved-jobs/', views.saved_job_list, name='saved_job_list'),
]
