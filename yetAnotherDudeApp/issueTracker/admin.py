from django.contrib import admin

from .models import *


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('code',)


@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('code',)


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'submitter',
                    'submitted_date', 'modified_date')
    list_filter = ('priority', 'status', 'submitted_date')
    search_fields = ('title', 'description',)


@admin.register(IssueSummary)
class IssueSummary(admin.ModelAdmin):
    change_list_template = 'admin/issue_summary_change_list.html'
    date_hierarchy = 'submitted_date'

    def has_add_permission(self, request):
        return False


