from django.shortcuts import redirect
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles or request.user.is_staff:
                return view_func(request,*args,**kwargs)
            else:
                return redirect("Administration:dashboard")
        return wrapper_func
    return decorator
