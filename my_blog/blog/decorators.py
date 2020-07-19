from django.http import HttpResponse
from django.shortcuts import redirect


def role_required(allowed_roles=[]):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):

            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('showblog')  
        return wrap
    return decorator