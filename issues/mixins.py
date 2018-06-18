from django.shortcuts import redirect
from django.views.generic import View


class ViewPermissionMixin(View):
    permission_code = None

    def dispatch(self, *args, **kwargs):
        if not self.request.user.has_perm(self.permission_code):
            return redirect('issues_list')
        return super().dispatch(*args, **kwargs)
