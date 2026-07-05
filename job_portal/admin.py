from django.contrib import admin
from .models import (
    Application,
    Company,
    Education,
    EmployerProfile,
    Experience,
    Job,
    JobCategory,
    JobSeekerProfile,
    Location,
    Resume,
    SavedJob,
    Skill,
)


@admin.register(JobSeekerProfile)
class JobSeekerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'experience')
    search_fields = ('user__username', 'position')


@admin.register(EmployerProfile)
class EmployerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'designation', 'company_position')
    search_fields = ('user__username', 'designation')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'owner_name', 'email', 'is_verified')
    list_filter = ('is_verified',)
    search_fields = ('company_name', 'owner_name', 'email')


@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('country', 'district', 'city')
    search_fields = ('country', 'district', 'city')


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'job_category', 'vacancy', 'deadline')
    list_filter = ('job_category', 'employment_type')
    search_fields = ('title', 'company__company_name')


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('jobseeker_profile', 'title', 'is_default', 'uploaded_at')
    list_filter = ('is_default',)
    search_fields = ('title', 'jobseeker_profile__user__username')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('jobseeker_profile', 'institution', 'degree')
    search_fields = ('institution', 'degree')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('jobseeker_profile', 'company_name', 'position', 'working_status')
    search_fields = ('company_name', 'position')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'jobseeker_profile', 'applied_at')
    list_filter = ('applied_at',)
    search_fields = ('job__title', 'jobseeker_profile__user__username')


@admin.register(SavedJob)
class SavedJobAdmin(admin.ModelAdmin):
    list_display = ('jobseeker_profile', 'job', 'saved_at')
    search_fields = ('job__title', 'jobseeker_profile__user__username')
