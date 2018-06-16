from django.contrib.auth.models import User
from django.db import models


class Status(models.Model):
    code = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'status'
        verbose_name_plural = 'statuses'

    def __str__(self):
        return self.code


class Priority(models.Model):
    code = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'priority'
        verbose_name_plural = 'priorities'

    def __str__(self):
        return self.code


class Issue(models.Model):
    title = models.CharField(max_length=100)
    submitted_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    submitter = models.ForeignKey(User, verbose_name='submitter', related_name="submitter", on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, verbose_name='assigned to', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, verbose_name='status', related_name="status", on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, verbose_name='priority', related_name="priority", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'issue'
        verbose_name_plural = 'issues'
        ordering = ('status', 'priority', 'submitted_date', 'title')


class IssueSummary(Issue):
    class Meta:
        proxy = True
        verbose_name = 'Issue Summary'
        verbose_name_plural = 'Issue Summary'

