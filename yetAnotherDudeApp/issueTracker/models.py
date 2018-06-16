from django.contrib.auth.models import User
from django.db import models


class Status(models.Model):
    code = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'status'
        verbose_name_plural = 'statuses'

    def __unicode__(self):
        return self.code


class Priority(models.Model):
    code = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'priority'
        verbose_name_plural = 'priorities'

    def __unicode__(self):
        return self.code


class Issue(models.Model):
    title = models.CharField(max_length=100)
    submitted_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    submitter = models.ForeignKey(User, verbose_name='submitter', related_name="submitter", on_delete=False)
    assigned_to = models.ForeignKey(User, verbose_name='assigned to', on_delete=False)
    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, verbose_name='status', related_name="status", on_delete=False)
    priority = models.ForeignKey(Priority, verbose_name='priority', related_name="priority", on_delete=False)

    class Meta:
        verbose_name = 'issue'
        verbose_name_plural = 'issues'
        ordering = ('status', 'priority', 'submitted_date', 'title')

    def __unicode__(self):
        return self.title
