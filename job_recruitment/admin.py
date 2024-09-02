from django.contrib import admin

from job_recruitment.models import *


# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    pass
