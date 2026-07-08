from django.conf import settings
from django.db import models


class JobSeekerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='jobseeker_profile',)
    bio = models.TextField(blank=True)
    dob = models.DateField(null=True, blank=True)
    permanent_province = models.CharField(max_length=100, blank=True)
    permanent_district = models.CharField(max_length=100, blank=True)
    permanent_municipality_name = models.CharField(max_length=150, blank=True)
    permanent_ward_no = models.CharField(max_length=20, blank=True)
    permanent_place = models.CharField(max_length=150, blank=True)
    temporary_province = models.CharField(max_length=100, blank=True)
    temporary_district = models.CharField(max_length=100, blank=True)
    temporary_municipality_name = models.CharField(max_length=150, blank=True)
    temporary_ward_no = models.CharField(max_length=20, blank=True)
    temporary_place = models.CharField(max_length=150, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    position = models.CharField(max_length=100, blank=True)
    experience = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Job Seeker: {self.user}"


class EmployerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='employer_profile',)
    designation = models.CharField(max_length=100, blank=True)
    company_position = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return f"Employer: {self.user}"


class Company(models.Model):
    company_name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    company_size = models.CharField(max_length=50, blank=True)
    founded_year = models.PositiveIntegerField(null=True, blank=True)
    location = models.ForeignKey(
        'Location',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='companies',
    )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name


class JobCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    country = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.city}, {self.district}, {self.country}"


class Job(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='jobs',
    )
    job_category = models.ForeignKey(
        JobCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='jobs',
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='jobs',
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    salary = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    employment_type = models.CharField(max_length=50, blank=True)
    experience = models.CharField(max_length=100, blank=True)
    vacancy = models.PositiveIntegerField(default=1)
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Resume(models.Model):
    jobseeker_profile = models.ForeignKey(
        JobSeekerProfile,
        on_delete=models.CASCADE,
        related_name='resumes',
    )
    title = models.CharField(max_length=255)
    resume_file = models.FileField(upload_to='resumes/')
    is_default = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    jobseeker_profile = models.ForeignKey(
        JobSeekerProfile,
        on_delete=models.CASCADE,
        related_name='educations',
    )
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=100, blank=True)
    field_of_study = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.degree} at {self.institution}"


class Experience(models.Model):
    jobseeker_profile = models.ForeignKey(
        JobSeekerProfile,
        on_delete=models.CASCADE,
        related_name='experiences',
    )
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=50, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    working_status = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.position} at {self.company_name}"


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    jobseeker_profile = models.ForeignKey(
        JobSeekerProfile,
        on_delete=models.CASCADE,
        related_name='applications',
    )
    resume = models.ForeignKey(Resume, on_delete=models.SET_NULL, null=True, blank=True)
    cover_letter = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Application for {self.job.title}"


class SavedJob(models.Model):
    jobseeker_profile = models.ForeignKey(
        JobSeekerProfile,
        on_delete=models.CASCADE,
        related_name='saved_jobs',
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='saved_by')
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Saved job: {self.job.title}"
