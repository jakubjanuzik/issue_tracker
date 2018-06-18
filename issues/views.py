# coding: utf-8
from django.db.models import Avg, F, Max, Min
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from issues.mixins import ViewPermissionMixin
from issues.models import Issue


class IssuesListView(ListView):
    model = Issue
    template_name = 'issue_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()

        average_completion_delta = Issue.objects.filter(
            completed=True
        ).aggregate(
            average_completion=Avg(
                F('completion_datetime') - F('creation_datetime')
            )
        )
        max_completion_delta = Issue.objects.filter(completed=True).aggregate(
            max_completion=Max(
                F('completion_datetime') - F('creation_datetime')
            )
        )
        min_completion_delta = Issue.objects.filter(completed=True).aggregate(
            min_completion=Max(
                F('completion_datetime') - F('creation_datetime')
            )
        )

        context['average_completion'] = self.get_delta_string(
            average_completion_delta['average_completion']
        )
        context['max_completion'] = self.get_delta_string(
            max_completion_delta['max_completion']
        )
        context['min_completion'] = self.get_delta_string(
            min_completion_delta['min_completion']
        )
        return context

    def get_delta_string(self, delta):
        hours, rem = divmod(delta.seconds, 3600)
        minutes, _ = divmod(rem, 60)
        return f'{delta.days} Days, {hours} hours and {minutes} minutes'


class CreateIssueView(ViewPermissionMixin, CreateView):
    template_name = 'issue_form.html'
    model = Issue
    permission_code = 'can_add_issue'
    fields = [
        'submitter',
        'solver',
        'description',
        'status',
        'category',
        'completion_datetime',
        'completed',
    ]
    success_url = reverse_lazy('issues_list')


class DeleteIssueView(ViewPermissionMixin, DeleteView):
    model = Issue
    success_url = reverse_lazy('issues_list')
    permission_code = 'can_delete_issue'


class UpdateIssueView(CreateIssueView, UpdateView):
    permission_code = 'can_edit_issue'
