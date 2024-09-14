from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from accounts.models import User, Candidate, Employer
from job_recruitment.models import Resume, Job, Application


class CandidateInline(admin.StackedInline):
    model = Candidate
    extra = 0


class EmployerInline(admin.StackedInline):
    model = Employer
    extra = 0


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = []

    def get_inlines(self, request, obj):
        candidate = Candidate.objects.filter(user=obj)
        if candidate.exists():
            self.inlines.append(CandidateInline)
            return self.inlines
        employer = Employer.objects.filter(user=obj)
        if employer.exists():
            self.inlines.append(EmployerInline)
            return self.inlines
        return self.inlines


class ApplicationInline(admin.TabularInline):
    model = Application
    extra = 0
    readonly_fields = ('candidate',)

    def has_add_permission(self, request, obj):
        return False


class ResumeInline(admin.TabularInline):
    model = Resume
    extra = 1


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    inlines = [ResumeInline, ApplicationInline]


class JobInline(admin.TabularInline):
    model = Job
    extra = 0
    fields = ('title', 'type', 'date_posted')


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    inlines = [JobInline]