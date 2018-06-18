# coding: utf-8
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path

from issues.views import (
    CreateIssueView,
    DeleteIssueView,
    IssuesListView,
    UpdateIssueView,
)

urlpatterns = [
    path('', IssuesListView.as_view(), name='issues_list'),
    path('issue/add/', CreateIssueView.as_view(), name='issue_add'),
    path('issue/<int:pk>/', UpdateIssueView.as_view(), name='issue_update'),
    path(
        'issue/<int:pk>/delete/',
        DeleteIssueView.as_view(),
        name='issue_delete',
    ),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
]
