from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined']
        read_only_fields = ['id', 'date_joined']


# Location Serializer
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'country', 'district', 'city']
        read_only_fields = ['id']


# Skill Serializer
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']
        read_only_fields = ['id']


# JobCategory Serializer
class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']


# Company Serializer
class CompanySerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)
    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(),
        source='location',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = Company
        fields = [
            'id',
            'company_name',
            'owner_name',
            'description',
            'website',
            'email',
            'phone',
            'company_size',
            'founded_year',
            'location',
            'location_id',
            'is_verified',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class CompanyDetailSerializer(CompanySerializer):
    jobs_count = serializers.SerializerMethodField()

    class Meta(CompanySerializer.Meta):
        fields = CompanySerializer.Meta.fields + ['jobs_count']

    def get_jobs_count(self, obj):
        return obj.jobs.count()


# Education Serializer
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'institution', 'degree', 'field_of_study', 'start_date', 'end_date']
        read_only_fields = ['id']


# Experience Serializer
class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            'id',
            'company_name',
            'position',
            'employment_type',
            'start_date',
            'end_date',
            'working_status',
            'description',
        ]
        read_only_fields = ['id']


# Resume Serializer
class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['id', 'title', 'resume_file', 'is_default', 'uploaded_at']
        read_only_fields = ['id', 'uploaded_at']


# JobSeekerProfile Serializer
class JobSeekerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = JobSeekerProfile
        fields = [
            'id',
            'user',
            'bio',
            'dob',
            'permanent_province',
            'permanent_district',
            'permanent_municipality_name',
            'permanent_ward_no',
            'permanent_place',
            'temporary_province',
            'temporary_district',
            'temporary_municipality_name',
            'temporary_ward_no',
            'temporary_place',
            'linkedin',
            'github',
            'position',
            'experience',
        ]
        read_only_fields = ['id', 'user']


class JobSeekerProfileDetailSerializer(JobSeekerProfileSerializer):
    user = UserDetailSerializer(read_only=True)
    educations = EducationSerializer(many=True, read_only=True)
    experiences = ExperienceSerializer(many=True, read_only=True)
    resumes = ResumeSerializer(many=True, read_only=True)

    class Meta(JobSeekerProfileSerializer.Meta):
        fields = JobSeekerProfileSerializer.Meta.fields + ['educations', 'experiences', 'resumes']


# EmployerProfile Serializer
class EmployerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = EmployerProfile
        fields = ['id', 'user', 'designation', 'company_position', 'phone', 'website']
        read_only_fields = ['id', 'user']


class EmployerProfileDetailSerializer(EmployerProfileSerializer):
    user = UserDetailSerializer(read_only=True)

    class Meta(EmployerProfileSerializer.Meta):
        pass


# Job Serializer
class JobSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    job_category = JobCategorySerializer(read_only=True)
    location = LocationSerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(),
        source='company',
        write_only=True,
    )
    job_category_id = serializers.PrimaryKeyRelatedField(
        queryset=JobCategory.objects.all(),
        source='job_category',
        write_only=True,
        required=False,
        allow_null=True
    )
    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(),
        source='location',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = Job
        fields = [
            'id',
            'company',
            'company_id',
            'job_category',
            'job_category_id',
            'location',
            'location_id',
            'title',
            'description',
            'salary',
            'employment_type',
            'experience',
            'vacancy',
            'deadline',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class JobDetailSerializer(JobSerializer):
    applications_count = serializers.SerializerMethodField()
    saved_count = serializers.SerializerMethodField()

    class Meta(JobSerializer.Meta):
        fields = JobSerializer.Meta.fields + ['applications_count', 'saved_count']

    def get_applications_count(self, obj):
        return obj.applications.count()

    def get_saved_count(self, obj):
        return obj.saved_by.count()


# Application Serializer
class ApplicationSerializer(serializers.ModelSerializer):
    job = JobSerializer(read_only=True)
    jobseeker_profile = JobSeekerProfileSerializer(read_only=True)
    resume = ResumeSerializer(read_only=True)
    job_id = serializers.PrimaryKeyRelatedField(
        queryset=Job.objects.all(),
        source='job',
        write_only=True,
    )
    jobseeker_profile_id = serializers.PrimaryKeyRelatedField(
        queryset=JobSeekerProfile.objects.all(),
        source='jobseeker_profile',
        write_only=True,
    )
    resume_id = serializers.PrimaryKeyRelatedField(
        queryset=Resume.objects.all(),
        source='resume',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = Application
        fields = [
            'id',
            'job',
            'job_id',
            'jobseeker_profile',
            'jobseeker_profile_id',
            'resume',
            'resume_id',
            'cover_letter',
            'applied_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'applied_at', 'updated_at']


class ApplicationDetailSerializer(ApplicationSerializer):
    job = JobDetailSerializer(read_only=True)
    jobseeker_profile = JobSeekerProfileDetailSerializer(read_only=True)

    class Meta(ApplicationSerializer.Meta):
        pass


# SavedJob Serializer
class SavedJobSerializer(serializers.ModelSerializer):
    job = JobSerializer(read_only=True)
    jobseeker_profile = JobSeekerProfileSerializer(read_only=True)
    job_id = serializers.PrimaryKeyRelatedField(
        queryset=Job.objects.all(),
        source='job',
        write_only=True,
    )
    jobseeker_profile_id = serializers.PrimaryKeyRelatedField(
        queryset=JobSeekerProfile.objects.all(),
        source='jobseeker_profile',
        write_only=True,
    )

    class Meta:
        model = SavedJob
        fields = [
            'id',
            'job',
            'job_id',
            'jobseeker_profile',
            'jobseeker_profile_id',
            'saved_at',
        ]
        read_only_fields = ['id', 'saved_at']


class SavedJobDetailSerializer(SavedJobSerializer):
    job = JobDetailSerializer(read_only=True)
    jobseeker_profile = JobSeekerProfileDetailSerializer(read_only=True)

    class Meta(SavedJobSerializer.Meta):
        pass
