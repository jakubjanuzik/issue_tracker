# coding: utf-8
from django.conf.urls import url
from django.urls import path

from issues.views import IssuesListView

urlpatterns = [path('', IssuesListView.as_view(), name='issues_list')]
