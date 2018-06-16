from django.contrib import admin
from django.db.models import Count

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
    list_filter = (
        'priority',
    )

    def has_add_permission(self, request):
        return False

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'total': Count('id'),
        }

        response.context_data['summary'] = list(
            qs.values('priority__code').annotate(**metrics)
        )

        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )

        return response
