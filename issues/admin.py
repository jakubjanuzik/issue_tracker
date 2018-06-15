from django.contrib import admin

from issues.models import Category, Issue, Status


class IssuesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, IssuesAdmin)
admin.site.register(Status, IssuesAdmin)
admin.site.register(Issue, IssuesAdmin)
