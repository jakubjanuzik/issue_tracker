# coding: utf-8
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from issues.models import Issue
from issues.mixins import ViewPermissionMixin


class IssuesListView(ListView):
    model = Issue
    template_name = 'issue_list.html'


class CreateIssueView(ViewPermissionMixin, CreateView):
    template_name = 'issue_form.html'
    model = Issue
    permission_code = 'can_add_issue'
    fields = [
        'submitter', 'solver', 'description', 'status', 'category'
    ]
    success_url = reverse_lazy('issues_list')


class DeleteIssueView(ViewPermissionMixin, DeleteView):
    model = Issue
    success_url = reverse_lazy('issues_list')
    permission_code = 'can_delete_issue'


class UpdateIssueView(CreateIssueView, UpdateView):
    permission_code = 'can_edit_issue'
