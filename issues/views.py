# coding: utf-8
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from issues.models import Issue


class IssuesListView(ListView):
    model = Issue
    template_name = 'issue_list.html'
