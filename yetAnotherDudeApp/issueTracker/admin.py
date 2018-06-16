from django.contrib import admin

from .models import *


class StatusAdmin(admin.ModelAdmin):
    list_display = ('code',)


admin.site.register(Status, StatusAdmin)


class PriorityAdmin(admin.ModelAdmin):
    list_display = ('code',)


admin.site.register(Priority, PriorityAdmin)


class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'submitter',
                    'submitted_date', 'modified_date')
    list_filter = ('priority', 'status', 'submitted_date')
    search_fields = ('title', 'description',)


admin.site.register(Issue, IssueAdmin)
