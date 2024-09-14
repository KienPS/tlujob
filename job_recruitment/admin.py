from django.contrib import admin

from job_recruitment.models import *


class ApplicationInline(admin.TabularInline):
    model = Application
    extra = 0
    readonly_fields = ('candidate',)

    def has_add_permission(self, request, obj):
        return False


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    pass


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    inlines = [ApplicationInline]


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    readonly_fields = ('candidate',)

    def has_add_permission(self, request):
        return False
