from django.conf import settings
from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=64)
    display_name = models.CharField(max_length=64)

    def __str__(self):
        return f'Status: {self.name}'


class Category(models.Model):
    name = models.CharField(max_length=64)
    display_name = models.CharField(max_length=64)

    def __str__(self):
        return f'Category: {self.name}'


class Issue(models.Model):
    submitter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='submitter',
    )
    solver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='solver',
    )
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    completion_datetime = models.DateTimeField()
    completed = models.BooleanField(default=False)
